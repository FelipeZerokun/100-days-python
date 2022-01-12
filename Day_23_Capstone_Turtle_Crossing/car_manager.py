from turtle import Turtle
from random import choice, randint
COLORS = ["yellow", "red", "blue", "green", "black", "gray", "purple", "brown"]
START_POS_Y = [-210, -150, -90, -30, 30, 90, 150, 210, 270]
START_POS_X = [300, 320, 340]
MOVE_SPEED = [10, 12, 14, 16, 18, 20]


class Car:
    def __init__(self):
        self.difficulty = 0
        self.car_list = []

    def create_car(self):
        rand_num =  randint(1, 4)
        if rand_num == 1:
            new_car = Turtle("square")
            new_car.color(choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.setheading(180)
            new_car.goto(choice(START_POS_X), choice(START_POS_Y))
            self.car_list.append(new_car)

    def move(self):
        for car in self.car_list:
            car.forward(choice(MOVE_SPEED) + self.difficulty)

