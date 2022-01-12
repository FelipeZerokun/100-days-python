from turtle import Turtle
STARTING_POSITION = (0, -270)
MOVE_DISTANCE = 30
FINISH_LINE = 250


class GameTurtle(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def reset_pos(self):
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.back(MOVE_DISTANCE)