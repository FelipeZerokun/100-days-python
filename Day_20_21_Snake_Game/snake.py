from turtle import Turtle


class Snake:

    def __init__(self):
        self.starting_position = [(0, 0), (-20, 0), (-40, 0)]
        self.snake_body = []
        self.moving_speed = 15
        self.starting_snake()
        self.snake_head = self.snake_body[0]

    def starting_snake(self):
        for pos in self.starting_position:
            self.add_segment(pos)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.snake_body.append(new_segment)

    def extend_snake(self):
        self.add_segment(self.snake_body[-1].position())

    def move_snake(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[seg_num].goto(self.snake_body[seg_num - 1].xcor(), self.snake_body[seg_num - 1].ycor())
        self.snake_head.forward(self.moving_speed)

    def move_up(self):
        if self.snake_head.heading() == 270:
            pass
        else:
            self.snake_head.setheading(90)

    def move_down(self):
        if self.snake_head.heading() == 90:
            pass
        else:
            self.snake_head.setheading(270)

    def move_right(self):
        if self.snake_head.heading() == 180:
            pass
        else:
            self.snake_head.setheading(0)

    def move_left(self):
        if self.snake_head.heading() == 0:
            pass
        else:
            self.snake_head.setheading(180)

    def reset_snake(self):
        for segments in self.snake_body:
            segments.goto(350, 350)
        self.snake_body.clear()
        self.starting_snake()
        self.snake_head = self.snake_body[0]