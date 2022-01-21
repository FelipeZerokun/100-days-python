# 100 Days of Python
## Project 34: Quizzler App

This project is a Quizz app that will requets questions from a database of this website: [Open Trivia Database](https://opentdb.com/). To get the API from this page, you can enter this link [here](https://opentdb.com/api_config.php)

This API requieres four parameters:
* amount of questions
* category 
* difficulty
* and type (here will be boolean for True or False queestions)

The first thing I did was to import the questions from the API with requests, and save them in a variable called question_data. This will be a list with diccionaries. Each dictionary will be a question, and what we need from the dictionaries is the "question" key and the "correct_answer" key. This will be in the data.py file.

I followed the same structure as in the Day 17 project: quiz game. 
