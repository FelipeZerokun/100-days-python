from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, start_pos):
        super().__init__()
        self.pos = start_pos
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.color("white")
        self.speed("fast")
        self.setheading(90)
        self.goto(x= self.pos, y= 0)

    def move_up(self):
        self.forward(10)

    def move_down(self):
        self.back(10)

    def reset_position(self):
        self.goto(x= self.pos, y= 0)

