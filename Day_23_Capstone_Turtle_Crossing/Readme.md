# 100 Days of Python
## Project 23: Turtle crossing Game

The second Capstone project of the course, and another classic game!

Using everything I have learnt from class inheritance and OOP programming, I will be recreating the famous game Frogger!

And just like the previous games, I started by creating classes for the different elements I need for the game.
For this project, I will need three elements: The turtle crossing the road, the cars and the scoreboard.

For the turtle class, it is almost the same as the paddle class. Inhering methods from the Turtle module, I just created three new methods. move_up and move_down methods to move the turtle up and down, and the reset_pos method to reset the turtle to its initial position.

For the car class, I made lists of different colores, speeds and positions. I made a create car method that will randomly pick values from these lists. So, every time the program creates a car, they will have different colors, speeds and starting positions. I added one attribute called difficulty. This variable will be added to the car speed. It begins at 0, and will go up every time the user wins a level.
One thing I noticed when I tried creating the cars, is that they spawned way too quickly. So, using the randint method from the random module, I made the probability of spawning a car 25%.
The other method in this class is the move method. This method will make each car object to move to the left at a random speed.

The scoreboard class is just the same as the Snake game and Pong game project. An invisible turtle object that shows text with the score for the user. I made a new class called game_over that will show a Game Over text in the middle of the screen if the user loses.

In the main.py I imported all these classes and the Time module as well. I created the screen object, and used the listen method so the program detects inputs from the keyboard. 
I made a while loop that will keep repeating as long as the user does not lose. Each loop will create a car, and stop the program for 0.1 seconds. Following the logic of the car class, every 0.1 seconds the class will have a 25% chance of creating a car. This is the best way I found to balance the amount of cars in the screen. 
The user can use the up and down arrows to move the turtle. If a car hits de turtle, is game over. If the turtle reacher the upper part of the screen, the user will pass to the next level. Every time the user finish a level, the difficulty attribute of the cars will be increased by 4, making the cars slightly faster.
The game will go on as long as the turtle does not gets hit by a car.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 100 Días de Python
## Proyecto 23: Juego de cruce de tortugas.

¡El segundo gran projecto del curso, y otro juego clásico!

Usando todo lo aprendido de herencia de clases y programación OOP, recrearé el famoso juego Frogger.

Y justo como los juegos anterior, comencé creando las clases para los distintos elementos necesarios para el juego.
Para este proyecto, se necesitan tres elementos: La tortuga que va a cruzar el camino, los carros y el puntaje.

Para la clase Turtle, es casi la misma que la clase Paddle del proyecto Pong. Heredando los métodos del módulo Turtle, sólo cree tres nuevos métodos. Los métodos move_up y move_down para que la tortuga se mueva hacia arriba y hacia abajo, y el método reset_pos que hará que la tortuga regrese a su posición inicial.

Para la clase Car, hice listas con distintos colores, velocidad y posiciones. Hice el método create_car que usará distintos valores de estas listas. Cada vez que el programa cree un carro, será de distinto color, con distinta velocidad y distinta posición inicial. Añadí un atributo llamado difficulty. Esta variable será añadida a la velocidad del carro. Inicia con un valor de 0, y aumentará cada vez que el usuario termine un nivel.
Una cosa que noté cuando probaba creando carros, es que aparecía demasiado rápido. Así que, usando el método randint del módulo random, hice que la probabilidad de que un carro aparezca sea del 25%.
El otro método en esta clase es el método move. Este método hará que se muevan los carros hacia la izquierda a una velocidad aleatoria.

La clase scoreboard es la misma que en el juego Snake y el juego Pong. Un objeto Turtle invisible que muestra un texto con el puntaje del usuario. Hice una nueva clase llamada game_over que mostrará un texto de Game Over en el medio de la pantalla si el usuario pierde.

En el archivo main.py importé todas estas clases y el módulo Time por igual. Cree un objecto Screen, y usé el método listen para que el programa detecte entradas del teclado.
Hice un bucle While que se repitá siempre y cuando el usuario no pierda. Cada bucle creará un carro, y detendrá el programa por 0.1 segundos. Siguiente la lógica dentro de la clase Car, cada 0.1 la clase tendrá un 25% de posibilidad de crear un caro. Esta es la mejor forma que encontré para equilibrar la cantidad de carros en la pantalla.
El usuario puede utilizar las flechas arriba y abajo para mover la tortuga. Si un carro golpea a la tortuga, se acaba el juego. Si la tortuga llega a la parte superior de la pantalla, el usuario pasará al siguiente nivel. Cada vez que el usuario termina un nivel, el atributo difficulty de todos los carros aumentará en 4, haciendo a todos los carros un poco más rápido.
