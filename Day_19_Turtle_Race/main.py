from turtle import Screen
from turtles import turtles_list  # I will be using a separate file for the turtles definition
from random import choice, randint

my_screen = Screen()
my_screen.setup(width=800, height=600)

# Input asking the user for their bet
user_bet = my_screen.textinput(title="Make your bet", prompt="Which Turtle is going to win? Enter a Color from the "
                                                             "rainbow: ")

# Do the setup for the turtles. I used a different file for the turtles objects creation. From 0 to 6, in order
#  of the rainbow color
separation = my_screen.window_height() / 7
starting_x = -350
starting_y = 250
for t in turtles_list:
    t.penup()
    t.goto(x=starting_x, y=starting_y)
    starting_y -= separation


# Now I will create a function for the random advance of the turtles
def random_advance(turtle_obj):
    speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # turtle_obj.forward(choice(speed))
    turtle_obj.forward(randint(1, 20))
    # It turned better to used Randint


# Now, use a while to make the turtles advance until the end of the Screen
turtle_finished = False
winner = None

while not turtle_finished:
    for t in turtles_list:
        random_advance(t)
        if t.xcor() > 365:
            turtle_finished = True
            winner = t.color()[0]

if winner == user_bet.lower():
    print("You win!")
else:
    print("You lose")

print(f"The winner is {winner}")

my_screen.exitonclick()
