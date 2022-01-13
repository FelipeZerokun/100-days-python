# 100 Days of Python
## Project 19-20: Snake Game

This is a two day project, and one of the most popular games for cellphones. Snake game.

For this project I learnt about and used class inheritance. Inheritance is useful when we need to copy other class attributes and methods. I will copy some methods from the Turtle class to make the food class and the scoreboard class.

The food class will inherit the form, the color and the movements methods, while the scoreboard class will inherit text methods. Same classes, but I inherit different things that I need for each one.

Firstly I worked on the snake body. I created the snake class in the snake.py file.
For the initial snake, I created three individual Turtle objects, and set their positions 20 pixels behind each other. This is done with the starting_snake and add_segment methods. The extend_snake segment will add one segment to the snake body, and this happens everytime the snakes "eats" one piece of food.
For the movement, the "head" of the snake will always be the one that moves, the second segment of the snake will take the previous head position, the third segments will take the second segments previous position, and so on. The move_up, move_down, move_right and move_left methods will move the snake's head. The move_snake method will make sure all the segments follow the head's movement. Finally, the reset_snake will delete all the segments and will make a new snake from the starting positions.

After that snake body, I made the food class. I inherited the methods from the Turtle class. The Methods I need the most are shape, penup, speed and goto. This way I make the turtle a small circle that will move to certain position really, really fast. The only method in this class is refresh, that will move the "food" to a random new position.

With some logic in the main.py the snake game can work perfectly, but I will add some text so the user can see the currect score and the highest score in the game. In the scoreboard.py I made another class that inherit from Turtle class. However, this class will not show a "turtle" particle in the screen, but will show some text. 
So I used the hideturtle and penup method so the user can't see where is this turtle object. I set the scoreboard position to the upper left of the screen. In the attributes definition I used the read() method, but if you do not have a file with the name used in the code, an error will show up. Either create a "txt" file with the name in your folder, or you can use the write() method. add_score method will add one to the score attribute, and the update_scoreboard method will clear the previous text and update the text with the new score. reset_scoreboard method will check the score at the end of the game, and if the actual score is higher than the highscore, it will modify the text with the new highscore, and set the score attribute back to 0.

With all the elements ready, the main.py will import all these classes. One really important module here is the time module. In the while loop, I use a sleep method so every loop the code stops for 0.1 seconds. I created a screen in black to simulated the original game. Every loop the snake will move in the direction it is facing. If the snake reaches the end of the screen, it is game over, and the snake will be reset to its original position. The user can use the arrows to change the facing direction of the snake. This is done by using screen.listen method, and the onkey method. In the screen will appear a random "food" circle, and every time the snake passes over the food, it will increase it size.
Also, if the snake's head touches any other of the snake's body segments, the game will end.

There are many new things in this project, so I recommend reviewing it line by line. The time method is really good when using a infinite loop, or a loop that repeats constantly so the user can see whats happening. If this module is not used, things will happen way too fast for a human to see whats going on in the screen.

Class inheritance is really good when I need to copy some methods from other class, and I don't really need to create it from scrap. In this project, the food class will use some classes from the turtle class and I just added some extra methods I needed. 

Finally, I used new methods from python. With the keywords "with" and "as" I can open, write and read external files. In this project, I am reading and writing into a "txt" file named scoreboard. This methods are really good to remember when you need to interacte with external files.


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

