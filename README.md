# thin-gbfs-world-bike-shares-material-d3-react-leaflet

# 🚀 A thin and low-network-use mobile web app for many common bike sharing systems. 🚀

https://github.com/coding-to-music/thin-gbfs-world-bike-shares-material-d3-react-leaflet

From / By James Yuzawa https://github.com/yuzawa-san

https://github.com/yuzawa-san/thin-gbfs

## Environment variables:

```java

```

## GitHub

```java
git init
git add .
git remote remove origin
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:coding-to-music/thin-gbfs-world-bike-shares-material-d3-react-leaflet.git
git push -u origin main
```

# :bike: thin-gbfs :bike:

https://thin-gbfs.appspot.com/

A thin and low-network-use mobile web app for many common bike sharing systems.

I enjoy biking while I travel. Unfortunately, I have grown tired using many bloated web and native apps whilst using limited international data plans.

The goals of this project are:

- cache static assets (tiles, system lists, station lists) heavily on the client side.
- be able to access a large number of open data sources for various popular bike sharing systems.
- transmit data from server to app using a compact format.
- cache system and station information server side to avoid hitting the source data API's too often.
- limit number of TCP connections and number of hosts contacted
- use HTTPS
- privacy: the HTML5 geolocation APi is used, but the location is not transmitted elsewhere.

## Development

Get google cloud sdk, load in dependencies using `npm install`.

There are more common tasks listed `npm run`.

To run a dev server: `npm run dev` and open your browser to localhost:8080.
You will need to seed the DB by going to localhost:8000, then cron jobs and then run the only cron job.

## Software License Info

In order to minimize the number of TCP connections between the web app and the server, the dependencies have been webpacked together.
These projects have been utilized and bundled:

- [material-ui](https://github.com/mui-org/material-ui/) ([MIT](https://github.com/mui-org/material-ui/blob/next/LICENSE))
- [d3-color](https://github.com/d3/d3-color/) ([BSD 3-clause](https://github.com/d3/d3-color/blob/master/LICENSE))
- [emoji-flags](https://github.com/matiassingers/emoji-flags) ([MIT](https://github.com/matiassingers/emoji-flags/blob/master/license))
- [leaflet](https://github.com/Leaflet/Leaflet) ([BSD 2-clause](https://github.com/Leaflet/Leaflet/blob/master/LICENSE))
- [react](https://github.com/facebook/react/) ([MIT](https://github.com/facebook/react/blob/master/LICENSE))
- [react-jss](https://github.com/cssinjs/jss/blob/master/packages/react-jss) ([MIT](https://github.com/cssinjs/jss/blob/master/packages/react-jss/LICENSE))
- [react-leaflet](https://github.com/PaulLeCam/react-leaflet/blob/master/LICENSE) ([MIT](https://github.com/PaulLeCam/react-leaflet/blob/master/LICENSE))

This project uses the MIT License.

## Credits

This web app simple aggregates and transmits efficiently across the wire lots of very useful data provided by various entities:

- [GBFS](https://github.com/NABSA/gbfs) - open API standard for (mostly large US) bike sharing systems
- [PyBikes](https://github.com/eskerda/pybikes) - a collection of various scrapers for various different API's
- [Citibik.es](https://api.citybik.es/) - api on top of pybikes

Thank you for your work!

Note: Since GBFS is an open standard, GBFS systems are hit directly rather than using Citibik.es.

### Data Errors

You will have to go to the respective projects / companies to their issue tracking systems. This project does not actually curate any data.
