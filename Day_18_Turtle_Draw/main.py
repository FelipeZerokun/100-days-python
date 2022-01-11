import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
# tim.color("red")

my_screen = Screen()
# my_screen.colormode(255)
turtle.colormode(255)


# Draw a straight line/dashed line
'''
for side in range(10):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
'''


def random_color():
    red_color = random.randint(1, 255)
    green_color = random.randint(1, 255)
    blue_color = random.randint(1, 255)
    return red_color, green_color, blue_color


# Draw other figures
'''

for num_sides in range(3, 8):
    # print(figures)
    angle = 360 / num_sides
    tim.color(random_color)

    for num_lines in range(1, num_sides + 1):
        # print(figures)
        tim.forward(100)
        tim.left(angle)
        # tim.forward(100)
'''

# Turtle Random Walk
'''
orientation = {"north": 0, "east": 90, "south": 180, "west": 270}
tim.pensize(15)
tim.speed(10)

for step in range(100):
    random_path = random.choice(list(orientation.values()))
    # print(random_path)
    tim.color(random_color())
    tim.setheading(random_path)
    tim.forward(random.randint(10, 40))
'''

# Turtle Spirograph
'''
tim.speed(0)
for degrees in range(0, 360, 5):
    tim.color(random_color())
    tim.setheading(degrees)
    tim.circle(radius=150.0)
'''

############ Turtle Painting project ############
# First, let's grab the colors we are going to use using Colorgram Package
import colorgram
colorgram_colors = colorgram.extract("dot_painting.jpg", 12)
my_colors = []
for color in colorgram_colors:
    colors = (color.rgb[0], color.rgb[1], color.rgb[2])
    my_colors.append(colors)
print(my_colors)
my_colors.pop(0)
my_colors.pop(0)
# print(my_colors)

# Secondly I will do the screen and turtle setups
my_screen.setup(width=600, height=600)
my_screen.setworldcoordinates(llx=0, lly=0, urx=600, ury=600)
tim.pensize(15)
tim.color(random.choice(my_colors))
tim.speed("fastest")
tim.penup()
tim.goto(0, 20)

# Now, the loop for drawing


def hor_drawing(n_steps):
    distance = int(my_screen.canvwidth / n_steps)
    tim.dot(size=25)
    tim.speed("slow")
    for gaps in range(int(tim.xcor()), my_screen.canvwidth, distance):
        tim.color(random.choice(my_colors))
        tim.forward(distance)
        tim.dot(size=25)
        # print(tim.xcor())

up_distance = 50
for h in range(0, my_screen.canvheight, up_distance):
    hor_drawing(10)
    tim.speed("fastest")
    tim.penup()
    tim.goto(x=0, y=tim.ycor() + up_distance)

print("Finished!")
tim.hideturtle()



my_screen.exitonclick()

