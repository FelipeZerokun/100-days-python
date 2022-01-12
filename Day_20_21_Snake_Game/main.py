from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Score

# First, Let's do the Screen setup
game_screen = Screen()
game_screen.setup(width=600, height=600)
game_screen.tracer(0)
game_screen.bgcolor("black")
game_screen.title("My Snake Game")

snake = Snake()
food = Food()
score = Score()


game_screen.listen()
game_screen.onkey(key="Up", fun=snake.move_up)
game_screen.onkey(key="Down", fun=snake.move_down)
game_screen.onkey(key="Left", fun=snake.move_left)
game_screen.onkey(key="Right", fun=snake.move_right)
game_on = True

while game_on:
    game_screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # Detect collision with food
    if snake.snake_head.distance(food) < 18:
        print("nom nom nom")
        food.refresh()
        snake.extend_snake()
        score.add_score()

    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or \
            snake.snake_head.ycor() < -280:
        print("Game over")
        # score.game_over()
        # game_on = False
        score.reset_scoreboard()
        snake.reset_snake()

    for segment in snake.snake_body[1:]:
        if snake.snake_head.distance(segment) < 1:
            print("Game over")
            # score.game_over()
            # game_on = False
            score.reset_scoreboard()
            snake.reset_snake()







game_screen.exitonclick()

