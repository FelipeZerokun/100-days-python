from turtle import Turtle

FONT = ("Ariel", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.user_score = -1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.user_score += 1
        self.reset()
        self.hideturtle()
        self.penup()
        self.goto(-220, 250)
        self.write(f"Score: {self.user_score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
