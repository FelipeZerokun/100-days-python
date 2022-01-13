# 100 Days of Python
## Project 19-20: Snake Game

This is a two day project, and one of the most popular games for cellphones. Snake game.

For this project I learnt about and used class inheritance. Inheritance is useful when we need to copy other class attributes and methods, but add some methods of your own.
I will copy some methods from the Turtle class to make the food class and the scoreboard class.

The food class will inherit the form, the color and the movements methods, while the scoreboard class will inherit text methods. Same classes, but I inherit different things that I need for each one.

Firstly I worked on the snake body. I created the snake class in the snake.py file.
For the initial snake, I created three individual Turtle objects, and set their positions 20 pixels behind each other. This is done with the starting_snake and add_segment methods. The extend_snake segment will add one segment to the snake body, and this happens everytime the snakes "eats" one piece of food.
For the movement, the "head" of the snake will always be the one that moves, the second segment of the snake will take the previous head position, the third segments will take the second segments previous position, and so on. The move_up, move_down, move_right and move_left methods will move the snake's head. The move_snake method will make sure all the segments follow the head's movement. Finally, the reset_snake will delete all the segments and will make a new snake from the starting positions.

After that snake body, I made the food class. I inherited the methods from the Turtle class. The Methods I need the most are shape, penup, speed and goto. This way I make the turtle a small circle that will move to different positions really, really fast. The only method in this class is refresh, that will move the "food" to a random new position.

With some logic in the main.py the snake game can work perfectly, but I will add some text so the user can see the currect score and the highest score in the game. In the scoreboard.py I made another class that inherit from Turtle class. However, this class will not show a "turtle" particle in the screen, but will show some text. 
So I used the hideturtle and penup method so the user can't see where is this turtle object. I set the scoreboard position to the upper left of the screen. In the attributes definition I used the read() method, but if you do not have a file with the name used in the code, an error will show up. Either create a "txt" file with the name in your folder, or you can use the write() method. add_score method will add one to the score attribute, and the update_scoreboard method will clear the previous text and update the text with the new score. reset_scoreboard method will check the score at the end of the game, and if the actual score is higher than the highscore, it will modify the txt file with the new highscore, and set the score attribute back to 0.

With all the elements ready, the main.py will import all these classes. One really important module here is the time module. In the while loop, I use a sleep method so every loop the code stops for 0.1 seconds. I created a screen in black to simulated the original game. Every loop the snake will move in the direction it is facing. If the snake reaches the end of the screen, it is game over, and the snake will be reset to its original position. The user can use the arrows to change the facing direction of the snake. This is done by using screen.listen method, and the onkey method. In the screen will appear a random "food" circle, and every time the snake passes over the food, it will increase it size.
Also, if the snake's head touches any other of the snake's body segments, the game will end.

There are many new things in this project, so I recommend reviewing it line by line. The time method is really good when using a infinite loop, or a loop that repeats constantly so the user can see whats happening. If this module is not used, things will happen way too fast for a human to see whats going on in the screen.

Class inheritance is really good when I need to copy some methods from other class, and I don't really need to create it from scrap. In this project, the food class will use some methods from the turtle class and I just added some extra methods I needed. 

Finally, I used new methods from python. With the keywords "with" and "as" I can open, write and read external files. In this project, I am reading and writing into a "txt" file named scoreboard. It is really good to remember this methods when you need to interacte with external files.


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 100 Días de Python
## Project 19-20: Juego de Snake

Este es un proyecto de dos días, y uno de los juegos más populares para celular. Juego de Snake.

Para este proyecto aprendí y usé herencia de clases. La herencia es realmente útil cuando necesitas copiar métodos y atributos de otras clases, y añadir métodos nuevos.
Voy a copiar algunos métodos de la clase Turtle para hacer las clases "food" y "scoreboard".

La clase "food" heredará los métodos de forma, color y movimiento, mientras que la clase "scoreboard" heredará métodos de texto. Heredo de la misma clase, pero cada una utiliza las cosas que más necesita.

Comencé trabajando en el cuerpo de la serpiente. Cree una clase snake en el archivo snake.py
Para la serpiente inicial, cree tres objetos turtle, y establecí sus posiciones iniciales 20 pixeles uno detras del otro. Esto se logra con los métodos starting_snake y add_segment. El método extend_snake añadirá un segmento al cuerpo de la serpiente, y esto ocurrirá cada vez que la serpiente "coma" una pieza de comida.
Para el movimiento, la "cabeza" de la serpiente siempre será la que se mueva, el segundo segmento irá a la posición previa de la cabeza, el tercer segmento toma la posición del segundo segmento y así sucesivamente. Los métodos de move_up, move_down, move_right y move_left se encargarán de mover la cabeza de la serpiente. El método move_snake se encargará de que los segmentos sigan el movimiento de la cabeza. Finalmente, reset_snake borrará todos los segmentos y hará una nueva serpiente en las posiciones iniciales.

Después del cuerpo de la serpiente, hice la clase "food". Heredé los métodos de la clase Turtle. Los métodos que necesito son shape, penup, speed y goto. De esta forma puedo hacer la tortuga un pequeño círculo that se moverá a distintas posiciones muy, muy rápido. El único método adicional es refresh, que hará que la "comida" se mueva a una nueva posición aleatoria.

Con algo de lógica en el archivo main.py el juego podría funcionar perfectamente, pero añadiré un texto para que el usuario pueda ver su puntaje actual y el puntaje más alto en el juego. En el archivo scoreboard.py hice otra clase que heredará de la clase Turtle. Sin embargo, esta clase no mostrará una "tortuga" en la pantalla, sino que mostrará algún texto. Así que usé los métodos hideturtle y penup para que el usuario no pueda ver el objeto Turtle. Ubiqué la posición del marcador en la parte superior izquierda de la pantalla. En la definición de atributos usé el método read(), pero si no tienen un archivo con el nombre usado en el código, un error aparecerá. Puedes crear un archivo "txt" con ese nombre en la carpeta del código, or puedes usar el método write(). El método add_score añadirá un punto al puntaje, y el método update_score borrará el texto previo y actualizará el texto con el nuevo puntaje. El método reset_scoreboard revisará el puntaje al final del juego, y si el puntaje actual es mayor que el puntaje más alto, modificará el archivo txt con el nuevo puntaje más alto, y regresará el atributo puntaje a cero.

Con todos los elementos listos, en el archivo main.py importaré todas estas clases. Un módulo realmente importante aquí es el módulo time. En el bucle while, usé el método sleep de forma que cada bucle el código se detiene por 0.1 segundos. Cree una pantalla en negro para simular el juego original. Cada bucle la serpiente se moverá en la dirección que esté mirando. Si la serpiente alcanza el final de la pantalla, será fin del juego, y la serpiente volverá a su posición original. El usuario puede usar las flechas para cambiar la dirección que la serpiente está mirando. Esto se logra al usar el método screen.list, y el método onkey. En la pantalla aparecerá un círculo de "comida" aleatoriamente, y cada vez que la serpiente pasa por encima de la comida, incrementará su tamaño.
También, si la cabeza de la serpiente toca cualquier segmento del cuerpo, el juego terminará.

Hay muchas cosas nuevas en este proyecto, así que recomiendo revisar el código linea por linea. El método de time es realmente útil cuando se usan bucles infinitos, o bucles que se repiten constantemente para que el usuario pueda ver lo que está sucediendo. Si este módulo no se usa, las cosas va a pasar muy rápido para que un humano pueda ver lo que pasa en la pantalla.

La herencia de clases es realmente bueno cuando necesitas usar métodos de otras clases, y así no se tiene que crear desde cero. En este projecto, la clase "food" usará algunos métodos de la clase Turtle y yo solo añado algunos métodos extra que necesité.

Finalmente, usé unos métodos de python. Con las palabras clave "with" y "as" puedo abrir, escribir y leer archivos externos. En este proyecto, estoy leyendo y escribiendo en un archivo "txt" llamado scoreboard. Es realmente bueno recordar estos métodos cuando necesitas interactuar con archivos extenos al proyecto.
