# 100 Days of Python
## Project 23: Turtle crossing Game

The second Capstone project of the course, and another classic game!

Using everything I have learnt from class inheritance and OOP programming, I will be recreating the famous game Frogger!

And just like the previous games, I started by creating classes for the different elements I need for the game.
For this project, I will need three elements: The turtle crossing the road, the cars and the scoreboard.

For the turtle class, it is almost the same as the paddle class. Inhering methods from the Turtle module, I just created three new methods. move_up and move_down methods to move the turtle up and down, and the reset_pos method to reset the turtle to its initial position.

For the car class, I made lists of different colores, speeds and positions. I made a create car method that will randomly pick values from these lists. So, every time the program creates a car, they will have different colors, speeds and starting positions. One thing I noticed when I tried creating the cars, is that they spawned way too quickly. So, using the randint method from the random module, I made the probability of spawning a car 25%.
The other method in this class is the move method. This method will make each car object to move to the left at a random speed.

The scoreboard class is just the same as the Snake game and Pong game project. An invisible turtle object that shows text with the score for the user. I made a new class called game_over that will show a Game Over text in the middle of the screen if the user losses.

In the main.py I imported all these classes and the Time module as well. I created the screen object, and used the listen method so the program detects inputs from the keyboard. 
I made a while loop that will keep repeating as long as the user does not lose. Each loop will create a car, and stop the program for 0.1 seconds. Following the logic of the car class, every 0.1 seconds the class will have a 25% chance of creating a car. This is the best way I found to balance the amount of cars in the screen. The user con use the up and down arrows to move the turtle. If a car hits de turtle, is game over. If the turtle reacher the upper part of the screen, the user will pass to the next level. 
