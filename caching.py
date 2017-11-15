from md5 import md5
import json
from google.appengine.api import urlfetch
from google.appengine.api import memcache
import logging

def url_key(url):
    return md5(url).hexdigest()

def cache(some_function):

    def wrapper(url, ttl):
        key = url_key(url)
        value = memcache.get(key)
        if value is None:
            value = some_function(url)
            try:
                added = memcache.add(key, json.dumps(value,separators=(',', ':')), ttl)
                if not added:
                    logging.error('Memcache set failed.')
            except ValueError:
                logging.error('Memcache set failed - data larger than 1MB')
            return value
        return json.loads(value)

    return wrapper

class MemcacheHolder:
    def __init__(self,etag,content_type,data):
        self.etag = etag
        self.content_type = content_type
        self.data = data

def http_cached(etag=False, ttl=0):
    def decorator(handler_func):
        def wrapper(*args, **kwargs):
            handler = args[0]
            request = handler.request
            response = handler.response
            uri = request.path
            key = url_key(uri)
            response.headers['Cache-Control'] = 'public,max-age=%d' % ttl
            holder = memcache.get(key)
            if holder is None:
                handler_func(*args, **kwargs)
                if response.status_int != 200:
                    return
                body = response.body
                holder = MemcacheHolder(md5(body).hexdigest(),handler.response.headers['Content-Type'],body)
                try:
                    added = memcache.add(key, holder, ttl)
                    if not added:
                        logging.error('Memcache set failed.')
                except ValueError:
                    logging.error('Memcache set failed - data larger than 1MB')
            else:
                response.headers['Content-Type'] = holder.content_type
                response.write(holder.data)
            if etag:
                response_etag = holder.etag
                response.headers['ETag'] = '"%s"' % response_etag
                request_etag = None
                if 'If-None-Match' in request.headers:
                    request_etag = request.headers['If-None-Match']
                    if request_etag.startswith('"') and request_etag.endswith('"'):
                        request_etag = request_etag[1:-1]
                if request_etag is not None and request_etag == response_etag:
                    response.status_int = 304
                    response.status_message = "Not Modified"
                    response.status = "304 Not Modified"
                    return
        return wrapper
    return decorator