from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed("fast")
        self.setheading(80)
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def ball_movement(self):
        new_x_cord = self.xcor() + self.x_move
        new_y_cord = self.ycor() + self.y_move
        self.goto(new_x_cord, new_y_cord)

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
        self.ball_speed *= 0.85

    def reset_position(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.ball_speed = 0.1
