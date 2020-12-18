# spotify-challenge
Shopify Developer Intern Challenge Question

## Initial Notes:
It is very funny that this was the challenge outlined! A year or two ago, I wanted an Instagram-alternative for displaying my photography.
Since I already owned several personal domains, it only made sense to make a system that worked with the rest of my webiste.

## How to run it!
Since the server is programmed with SSL, you will be unable to run it locally. Instead, I have included a link to one of my servers where it is being hosted.
[SketchThis.ca/photos](http://sketchthis.ca/photos)

## Technical Analysis

### How do you manage all of the photos!?
Let's start with the most simple way to accomplish this: An HTML page, with <img> tags. Is this a viable option? 
Sure, if you have only 5 or 10 photos, you don't want dynamic pages, ways to filter the photos, etc. But if you do want these features, you need to do something different.

This is where a more dynamic approach comes into play, and this is how I chose to solve the problem: Use an API to allow the front-end to access the photo information that is stored in a database, use front-end scripting and dynamic endpoints to load photos onto those pages as required.

All in all, we will need:
- A webserver that supports custom routing (Tornado Web Server, Python3)
- Some sort of database
- Photos to host
- Some time to program!
