# 100 Days of Python
## Project 11: Blackjack game

The first Capstone project in the course.
Another really popular game, the Blackjack Game!

This project uses all the knowledge from the projects before.
* import data from other files
* User inputs
* Type conversion
* Function creation and calling
* Data Structure -Lists
* Loops - While If

Firstly, I created a file called card_selection.py where I made a function that will randomly pick a card from A to K, like a deck of cards.
I made a pretty simple game where the user will play against the computer. The player will have two cards, and can ask for more cards. 
If the number of the cards in the user "hand" exceeds 21, the player loses. The player can stop drawing at any time. After this the program will compare the sum of the player cards and the computer cards, and the one with higher sum wins. There can also be a tie.

There is a small trick here. The Ace can be used either as a 11 or 1. So, there is a small condiction. If the sum of the player or computer is below 21 while the Ace is counted as 11, nothing happens. But if the sum goes above 21 the ace will be counted as a 1. At first, this is a bit complicated to traslate to the code, but it was a really good practice.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 100 Días de Python
## Proyecto 11: Juego de veintiuno.


El primer proyecto grande del curso.
!Otro juego muy popular, veintiuno o BlackJack!

Este proyecto utiliza todo el conocimiento adquirido de proyectos anteriores.
* importar data de otros archivos.
* Ingreso de información de usuario.
* Conversión de tipo
* Creación y llamado de funciones.
* Estructura de datos - Listas
* Bucles - While If

Primeramente, cree un archivo llamado card_selection.py dónde hice una función que va a escoger una carta aleatoreamente desde el As hasta la K, como una baraja de cartas.
Luego, hice un juego realmente simple dónde el usuario juega contra el ordenador. El jugador tendrá dos cartas, y puede pedir más.
Si el número de cartas en la "mano" del usuario excede la suma de 21, el jugador pierde. El jugador puede dejar de tomar cartas en cualquier momento. Después de esto, el programa va a comparar la suma de las cartas del jugador con las del ordenador, y aquel cuya suma sea superior gana. También puede haber un empate

Hay un pequeño truco aquí. El As puede ser usado como 11 o como 1. Así, que debe haber una pequeña condición. Si la suma de las cartas del jugador o del ordenador es 21 o menos con el As, éste será sumado como 11, y no pasa nada. Pero si la suma es superior a 21 el As será sumado como un 1. Al inicio, esto es un poco complicado de plasmar como código, pero fue una práctica realmente buena.
