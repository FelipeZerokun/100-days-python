from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(x=-100, y=200)
        self.write(self.left_score, align="center", font=("Courier", 80, "normal"))
        self.goto(x=100, y=200)
        self.write(self.right_score, align="center", font=("Courier", 80, "normal"))

    def l_score(self):
        self.left_score += 1
        self.update_score()

    def r_score(self):
        self.right_score += 1
        self.update_score()