# 100 Days of Python
## Project 25: States game

Here I learnt how to use CSV files!
CSV (Comma-separated value) is a delimited text file that separates values using commas. This is a pretty common way to store and share tabular data, o a single relationship database.
Here I will be using one of the most common and useful libraries in python for Data manipulation. Used in data science and data analytics.

I made a small project before the main one, and I uploaded because it was really interesting for me. So, I will explain the small project first, before the States game project.

The Great Squirrel Census project was a really interesting project from [The squirrel Census](https://www.thesquirrelcensus.com/), where numerous volunteers went to the Central Park to count up all the squirrels in the park. This lead to an amazing squirell database here: [NYC Open data](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw).
In this database, you can see many characteristics like, age, fur color, location, behaviour, and much more. So, using this database I practiced how to manage a CSV file using Python. Our objective is to count up how many squirrels from each color are in this database. The fur colors are Gray, cinnamon and black.

Before anything, you must install the pandas library in your IDE, and then import it to the project.
using the read_csv method from Pandas I imported the Squirrel CSV file into a variable. This variable will be a Pandas object.
