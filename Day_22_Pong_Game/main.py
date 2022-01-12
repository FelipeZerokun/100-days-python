from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

my_screen = Screen()
my_screen.title("PONG")
my_screen.bgcolor("black")
my_screen.setup(width=800, height=600)
my_screen.tracer(0)

left_paddle = Paddle(-350)
right_paddle = Paddle(350)
game_ball = Ball()
my_scoreboard = Scoreboard()

my_screen.listen()
# Right Paddle
my_screen.onkeypress(key="Up", fun=right_paddle.move_up)
my_screen.onkeypress(key="Down", fun=right_paddle.move_down)
# Left paddle
my_screen.onkeypress(key="w", fun=left_paddle.move_up)
my_screen.onkeypress(key="s", fun=left_paddle.move_down)

game_is_on = True
while game_is_on:
    time.sleep(game_ball.ball_speed)
    my_screen.update()
    game_ball.ball_movement()

    # Detect collision with top and bot "walls"
    if game_ball.ycor() > 280 or game_ball.ycor() < -280:
        game_ball.wall_bounce()

    # Detect collision with each paddle
    if (game_ball.distance(right_paddle) < 50 and game_ball.xcor() > 320) or (game_ball.distance(left_paddle) < 50 and
                                                                              game_ball.xcor() < -320):
        game_ball.paddle_bounce()
        print(f"Actual speed is: {game_ball.ball_speed}")

    # Detect when Ball goes in Goal
    if game_ball.xcor() > 380:
        print("GOAL!")
        game_ball.reset_position()
        right_paddle.reset_position()
        left_paddle.reset_position()
        my_scoreboard.l_score()
        time.sleep(2)

    elif game_ball.xcor() < -380:
        print("GOAL!")
        game_ball.reset_position()
        right_paddle.reset_position()
        left_paddle.reset_position()
        my_scoreboard.r_score()
        time.sleep(2)




my_screen.exitonclick()