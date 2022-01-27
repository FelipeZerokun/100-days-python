# 100 Days of Python
## Project 38: Workout tracking APP

A simple app that will keep track of different exercise you do in a day.
Using a natural language processing from [Nutritionix](https://www.nutritionix.com/) I did an app that will take a text from the user and will save the information in a Google Spreadsheet.

The information saved will be:
* Type of exercises done.
* duration of each exercise
* Estimated calories burnt
* The date

I will be using [Sheety](https://sheety.co/) to connect into my Google spreadsheets, and save all this information for me.

The first step was to setup the Nutritionix connection. I created an account, and got my user ID and a API key. This is needed for the headers authentication part.

I used the Natural Language endpoint to get the data I needed. [Here](https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/edit#) is the documentation for it, in the Exercise Endpoints section.
Also [here](https://gist.github.com/mattsilv/d99cd145cc2d44d71fa5d15dd4829e03) is an Example of how to use this enpoint. 
Providing the user's information, the request will return a json file with all the data I need. I stored each data I needed in different variables.
