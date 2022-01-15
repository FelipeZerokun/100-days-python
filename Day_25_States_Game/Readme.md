# 100 Days of Python
## Project 25: States game

Here I learnt how to use CSV files!
CSV (Comma-separated value) is a delimited text file that separates values using commas. This is a pretty common way to store and share tabular data, o a single relationship database.
Here I will be using one of the most common and useful libraries in python for Data manipulation. Used in data science and data analytics.

I made a small project before the main one, and I uploaded because it was really interesting for me. So, I will explain the small project first, before the States game project.

The Great Squirrel Census project was a really interesting project from [The squirrel Census](https://www.thesquirrelcensus.com/), where numerous volunteers went to the Central Park to count up all the squirrels in the park. This lead to an amazing squirell database here: [NYC Open data](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw).
In this database, you can see many characteristics like, age, fur color, location, behaviour, and much more. So, using this database I practiced how to manage a CSV file using Python. Our objective is to count up how many squirrels from each color are in this database. The fur colors are Gray, cinnamon and black.

Before anything, you must install the pandas library in your IDE, and then import it to the project.
using the read_csv method from Pandas I imported the Squirrel CSV file into a variable. This variable will be a Pandas object known as a dataframe. It is similar to a list. With the conditional ["Primary Fur Color"] == "Color" I can get all the column that match the "color". So, I just did the comparisson with the three colors, and used the len method to count how many were on each one. 
Finally, to learn how to transform this data into a CSV file, DataFrame and the to_csv methods with the data I got.

Now, the States Game project
Basically, it is a game where you have to point out all the states in a map of the United States of America.
To make this game dinamic, I used the Screen method from the Turtle module. Using the addshape method I can use a image as a background for the screen. 
I used a NameTheState class that will create an invisible Turtle object that will have a text with the name of each state. The map will begin empty, and every time the user enters the name of a State, the text with the name will appear in the map. The only method in this class is write_state_name, which will move the turtle object to certain coords in the map and show a text with the State's name.
To know exactly where each state is in terms of X and Y coords, I created a function in the main.py file called get_mouse_click_coor that will return the coordinates of the mouse when I click somewhere in the map. This way I can get all the States coords in the map. I created a CSV file that will have all the states with their own coords separated by comma. After getting the coords of all 50 states, I commented out the function. 
Again, I will be using Pandas for the CSV file reading.
I will use a While loop for the duration of the game. I will ask the user the enter the name of a State with input. Then, I will import all the states from the CSV file using Pandas method read_csv. Then I will compare the user's answer with each state on the list. If the User's answer is an actual State and it is not in the map yet, then I will call the write_state_name method. 
If the user gets all 50 states, the game ends. The user may also exit the game. By doing this, the program will check all the states the user didn't get and save them in a different CSV file for the user to know which States he missed. 
Finally, the program will print how many states did the user get.
