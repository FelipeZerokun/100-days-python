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
