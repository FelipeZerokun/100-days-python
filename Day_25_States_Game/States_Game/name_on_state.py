from turtle import Turtle

FONT = ("Ariel", 7, "normal")


class NameTheState(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def write_state_name(self, state_name, x_pos, y_pos):
        self.goto(x= x_pos, y= y_pos)
        self.write(state_name, align="center", font=FONT)
