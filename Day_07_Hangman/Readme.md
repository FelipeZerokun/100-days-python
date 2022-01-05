# 100 Days of Python
## Project 7: Hangman game

Another classic game in Python!
The Hangman is a popular game where the user tries to guess the hidden word without too many mistakes.
This is the first project where I divide it into multiple files. In this case, I used three files:
* main.py is where the code for the game is written.
* hangman_art.py where I stored some ASCII art for the game.
* hangman_words.py where I stored a list of words that will be used for the game.

First of all, using "import" I make all the files usable in the main.py.

Now, the program will take one random word from the word_list from the hangman_words.py. In a new variable, I will add as many underscores (_) as letters in the choosen word.
The user will have 6 lives, and everytime the user fails to guess a letter in the word, a life will be substracted. For every life, there is a different art.

The game continues until the user guesses the word, or there are no more lives.

This project is another excelent practice for programming logic, and to begin to understand how to get certain objects from external files.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 100 Días de Python
## Proyecto 7: Juego del ahorcado

!Otro juego clásico en Python!
El ahorcado es un juego muy popular dónde el usuario intenta adivinar una palabra oculta sin cometer muchos errores.
Éste es el primer proyecto dónde lo divido en múltiples archivos. En este caso, utilicé tres archivos:
* main.py es dónde está escrito el código para el juego.
* hangman_art.py es dónde está guardado arte ASCII para el juego.
* hangman_words.py es dónde está una lista con las palabras para el juego.

Primero que nada, utilizando "import" hago que todos los archivos sean usables en main.py

Ahora, el programa tomará una palabra aleatoria de la lista de palabras word_list del archivo hangman_words.py. En una nueva variable, añadiré tantos guiones bajos (_) como letras haya en la palabra escogida.
El usuario tendrá 6 vidas, y cada vez que falle en adivinar una letra de la palabra, se restará una vida. Por cada vida, hay un arte diferente.

El juego continuará hasta que el usuario adivine la palabra, o no tenga más vidas.

Este proyecto es otra excelente práctica para la lógica de programación, y para empezar a entender cómo obtener ciertos objetos de archivos externos.
