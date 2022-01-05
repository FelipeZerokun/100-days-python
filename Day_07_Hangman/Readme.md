# 100 Days of Python
## Project 7: Hangman game

Another classic game in Python!
The Hangman is a popular game where the user tries to guess the hidden word without too many mistakes.
This is the first project where I divide it into multiple files. In this case, I used three files:
* main.py is where the code for the game is written.
* art.py where I stored some ASCII art.
* hangman_words.py where I stored a list of words that will be used for the game.

First of all, using "import" I make all the files usable in the main.py.

Now, the program will take one random word from the word_list from the hangman_words.py. In a new variable, I will add as many underscores (_) as letters in the choosen word.
The user will have 6 lives, and everytime the user fails to guess a letter in the word, a life will be substracted. For every life, there is a different art.

The game continues until the user guesses the word, or there are no more lives.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


