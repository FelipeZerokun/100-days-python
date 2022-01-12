from turtle import Screen
from my_turtle import GameTurtle
from scoreboard import Scoreboard
from car_manager import Car
import time

game_screen = Screen()
game_screen.setup(width=600, height=600)
game_screen.tracer(0)

turtle = GameTurtle()
my_scoreboard = Scoreboard()
game_screen.listen()

game_screen.onkey(fun= turtle.move_up, key="Up")
game_screen.onkey(fun= turtle.move_down, key="Down")

game_on = True
my_car_manager = Car()

while game_on:

    time.sleep(0.1)
    game_screen.update()
    my_car_manager.create_car()
    my_car_manager.move()

    for car in my_car_manager.car_list:
        if turtle.distance(car) < 20:
            print("HIT!")
            game_on = False
            my_scoreboard.game_over()

    if turtle.ycor() > 250:
        print("Next level!")
        turtle.reset_pos()
        my_scoreboard.update_scoreboard()
        my_car_manager.difficulty += 4
        time.sleep(1)
















game_screen.exitonclick()