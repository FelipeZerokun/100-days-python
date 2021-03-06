# 100 Days of Python
## Project 22: Pong Game

Another classic game for the game lovers like me! 
Following the same steps from the snake game project, this project can be done with ease.
The elements I need for the project are a ball, two paddles and a scoreboard.

So, following the snake game steps, I made the ball class inheriting the methods from the Turtle class. I changed its form to be round, white color and fast speed. 
For the movement motion, the ball will always advance 10 pixels on X and 10 pixels on Y. This will make the ball to always move diagonally at 45 degrees. The code for this is in the ball_movement method.
If the x_move variable is positive, the ball will move to the right, otherwise it will move to the left. If the y_move variable is positive, the ball will move upwards, otherwise it will move downwards. The methods wall_bounce and paddle_bounce will change the x_move and y_move signs. Also, every time the ball bounces on a paddle, the speed will be increased a bit.
When the ball goes beyond the left or right side of the screen, it counts as a point to a player, and the ball resets its position with the reset_position method.

Now for the paddles, they will also be created from a class that inherits from the turtle module. In this case, the shape will be rectangular. The methods move_up and move_down will make the paddes move up and down. The reset position will move the paddles back to the middle when a "goal" is made.

The scoreboard class is also a child from the Turtle class. Like the snake game, the scoreboard will be in the upper left side of the screen. Each player will have a score, and the update_score method will update any score.

So, in the main.py file, I create the screen that will be used for the game. Again, I made it black so it resembles the original game. I imported all the classes I created, and also the Time module. In a while loop, I used the sleep method with a variable from the ball class. Like I explained in the ball class part, everytime the ball bounces on a paddle, the speed will be increased. To achieve this, I used that variable to make the sleep time less and less every time, so it seems the game keeps getting faster.
Since there are two players for this game, I have to create two Paddle objects. One positioned to the left and one to the right.
Then with IFs conditionals the code will check if the ball goes beyond the left and right sides of the screen, or if it bounces on the roof, floor or the paddles.

Another good example of how to use inherited classes, and how to practice objects creation to make easy a project that would be kind of difficult.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 100 D??as de Python
## Proyecto 22: Juego Pong

??Otro juego cl??sico para los amantes de juegos como yo!
Siguiendo los mismos pasos del proyecto del juego Snake, este proyecto puede ser realizado con facilidad.
Los elementos necesarios para este proyecto son una pelota, dos paletas y un tablero de puntos.

As?? que, siguiendo los pasos del juego Snake, hice que la clase Ball herede los m??todos de la clase Turtle. Cambi?? su forma a un c??rculo, color blanco y velocidad r??pida.
Para el movimiento, la bola siempre avanzar?? 10 pixeles en X y 10 pixeles en Y. Esto har?? que la bola siempre se mueva diagonalmente a 45 grados. El c??digo para esto est?? en el m??todo ball_movement.

Si la variable x_move es positiva, la bola se mover?? hacia la derecha, de otra forma, se mover?? a la izquierda. Si la variable y_move es positiva, la bola se mover?? hacia arriba, de otra forma, se mover?? hacia abajo. Los m??todos wall_bounce y paddle_bounce cambiar??n los signos de las variables x_move y y_move. Tambi??n, cada vez que la bola rebote en una paleta, la velocidad ser?? incrementada un poco.
Cuando la bola se va m??s all?? del l??mite derecho e izquierdo de la pantalla, cuenta como un punto para un jugador, y la bola resetea su posici??n con el m??todo reset_position.

Ahora para las paletas, tambi??n ser??n creadas de una clase que hereda del m??dule Turtle. En este caso, la forma ser?? rectangular. Los m??todos move_up y move_down har??n que las paletas se muevan hacia arriba y hacia abajo. El reinicio de posici??n har?? que las paletas regresen al centro despu??s de un "gol".

La clase para el puntaje tambi??n heredar?? de la clase Turtle. Como en el juego Snake, el puntaje estar?? en la parte superior izquierda de la ventaja. Cada jugador tendr?? su propio puntaje, y el m??todo update_score actualizar?? cualquier puntaje.

As?? que, en el archivo main.py, crear?? la ventaja que ser?? usada para el juego. Nuevamente la crear?? de color negro para que se asemeje al juego original. Import?? todas las clases creadas, y tambi??n el m??dulo Time. En el bucle While, us?? el m??todo Sleep con una variable de la clase Ball. C??mo expliqu?? en la parte de la clase Ball, cada vez que la bola rebote en una paleta, la velociudad ser?? incrementada. Para lograr esto, us?? una variable que haga el tiempo de Sleep cada vez menor, haciendo que parezca que el juego se vuelve m??s r??pido.
Ya que hay dos jugadores para este juego, debo crear dos objetos Paddle. One posicionado a la izquierda y uno a la derecha.
Luego con condicionales IF el c??digo revisar?? cuando la bola se vaya por fuera de la pantalla a la izquierda o derecha, si rebota en el techo o en el piso, o si rebota en una paleta.

??ste es otro buen ejemplo en c??mo usar la herencia de clases, y para practicar la creaci??n de objetos para hacer un proyecto, 
