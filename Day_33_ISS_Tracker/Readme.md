# 100 Days of Python
## Project 33: ISS Tracker

This project will track the ISS [(International Space Station)](https://www.nasa.gov/mission_pages/station/main/index.html) via their API. If the Space Station is close to our position, and it is dark, the program will send an email telling you to watch up in the sky to see the Space Station.

An API [(Application Programming Interface)](https://en.wikipedia.org/wiki/API) is an interface that allows two applications to communicate with each other. This means that any application could receive or send data through this connection.

There are several web pages or companies that offer connectivity to their APIs, free or paid, and they send you different kind of data. In this case, I will be requesting data to the ISS asking for their coordinates. 

To do this, the requests library is needed. Also, the URL from the website we want to get the data is necessary. Here is the [API](http://api.open-notify.org/iss-now.json) for the ISS position.
I made an infinite loop that will check the ISS position every minute. 

Now, to check at what time is the sunset where I am, I used another API from a page called [unrise-sunset](https://www.sunrise-and-sunset.com/en). Here you can see the estimated sunrise and sunset times of different cities. To use this site APIs I need to provide the latitude and longitude of the city I want to check. In [latlong.net](https://www.latlong.net/) website I can check the coordinates of any place in the world. I saved the coordinates in a dictionary called parameters, which I used for the Sunrise Sunset API.

Now with both conditions, I just need to compare ISS coordinates with my coordinates, and if the time is past sunset and before sunrise, the app will send an email using the SMTP method.

This project is a really good introduction to APIs, which can be a powerful tool to get data from other sites.

