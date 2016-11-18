# Live-Events-Earthquake-map-using-in-Google-Maps-using-Django

This website shows live map of events like Earthquake, Landslide, Volcano and Forest Fire.
The data is extracted from www.usgs.gov using python scripts.
Currently this supports only earthquake, you can extent the same project to add more events as mentioned above.

Code is completely based on Django app.

The earthquake.kml file in static folder is for adding network link in Google Earth. This file is updated in every url requests.

For adding this kml file as a network link in google earth refer any online documentaion (I prefer the video in youtube by Dustin Hawkes: How to use network links with Google Earth and Dropbox, this video is for adding kml file in added in dropbox, you may have to update the dropbox part with what ever server you are keeping your kml file. Video link: https://www.youtube.com/watch?v=zeVvqiLNwto )
