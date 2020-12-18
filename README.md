# shopify-challenge
Shopify Developer Intern Challenge Question

## How to run it!
Make sure to have python3 installed, as well as tornado web server (pip install tornado).
Clone this repo, and run ```sudo python server.py``
In your browser navigate to ```127.0.0.1:80```
### Or, 
you can simply check out my demo:
[SketchThis.ca/photos](http://sketchthis.ca/photos)

## Technical Analysis

### How do you manage all of the photos!?
Let's start with the simplest way to accomplish this: 
An HTML page, with <img> tags. 
Is this a viable option? 
Sure, if you have only 5 or 10 photos, you don't want dynamic pages, ways to filter the photos, etc. But if you do want these features, you need a better way to store and load the images.

This is where a more dynamic approach comes into play. My strategy is to use database-ish type structure (more on that later) and use dynamic URL endpoints to tell the server what filtering on the photos is desired and how it should be displayed.

All in all, we will need:
- A web server that supports custom routing
- Some sort of database
- Photos to host
- Some time to program!
