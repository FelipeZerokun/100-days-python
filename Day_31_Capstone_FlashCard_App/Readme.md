# 100 Days of Python
## Project 31: Flashcard App

The third Capstone project in the course.

This is a flashcard app for learning japanese vocabulary!
I am a Japanese culture enthusiast, and I have been learning japanese for a couple years now, so for my flashcard app I decided to make it for learning Japanese Kanji characters.
For the Kanjis database, I grab some json databases from [David Gouveia](https://github.com/davidluzgouveia) github's proyect [Kanji data](https://github.com/davidluzgouveia/kanji-data). He has some good proyects, go and check them!

Using flashcards is a good technique for vocabulary learning. In this app, a flashcard with a random Kanji will be shown to the user, then the user will have three seconds to recognize the kanji before the flashcard turns and shows the Kanji's meaning. If the user knows the Kanji meaning, he/she should click the check button, otherwise he/she should click the X button. The app will remember which Kanjis the user didn't know and save them in a CSV file. 

This project is divided into four parts to make it more understandable. 

The first part was to make the UI. For this I used four images. One for the "correct" button, one for the "wrong" button, one for the front card and one for the back card.
I will be using Tkinter module for the UI.

Firstly I created a window using a Tk object. I made a main Canvas that will have the Japanese Kanji, with both on'yomi and kun'yomi readings. On'yomi is the chinese way to read a kanji, and kun'yomi is the japanese way to read a kanji. The main window will have a after method that will execute a function after 3000 miliseconds (or 3 seconds). This function will be flip_card, which will change the canvas a bit, showing the english meaning of the Kanji previously shown to the user.

