Using the Reeborg's World functions, I used the "hug the right wall" logic to escape the maze.
Although there could be scenarios where the robot is near the exit and moves away from it, it will always find the exit. 

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
