import another_module
from turtle import Turtle, Screen
import prettytable

#print(another_module.another_variable)

'''
#timmy = turtle.Turtle()
timmy = Turtle()
timmy.shape("turtle")
timmy.color("red", "cyan")
timmy.forward(50)

#print(timmy)
my_screen = Screen()
#print(my_screen.canvwidth)
my_screen.exitonclick()
'''

my_table = prettytable.PrettyTable()

my_table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander", "Bulbasour"])
my_table.add_column("Type", ["Electric", "Water", "Fire", "Grass"])
my_table.align = "l"
print(my_table)

