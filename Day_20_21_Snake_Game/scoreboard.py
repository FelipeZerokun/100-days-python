from turtle import Turtle

ALINGMENT = "center"
FONT = ("Courier", 24, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.player_score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())

        self.color("white")
        self.goto(0, 260)
        self.update_scoreboard()

    def add_score(self):
        self.player_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.player_score} High Score: {self.high_score}", False, align=ALINGMENT, font=FONT)

    # def game_over(self):
    #     self.clear()
    #     self.goto(0, 0)
    #     self.write(f"\tGAME OVER.\n Your final score is = {self.player_score}", False, align=ALINGMENT, font=FONT)

    def reset_scoreboard(self):
        if self.player_score > self.high_score:
            self.high_score = self.player_score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.player_score = 0
        self.update_scoreboard()

