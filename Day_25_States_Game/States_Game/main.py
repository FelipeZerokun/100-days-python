import turtle

import pandas

game_screen = turtle.Screen()
game_screen.setup(width=780, height=520)
game_screen.bgcolor("black")
game_screen.title("U.S. State Game")
background = "blank_states_img.gif"
game_screen.addshape(background)
turtle.shape(background)

# CODE TO GET X AND Y COORDINATES ON CLICK OF THE MOUSE ON SCREEN
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)

import pandas as pd
from name_on_state import NameTheState

game_on = True
name_state = NameTheState()
states_check_list = []

while game_on:
    user_answer = game_screen.textinput(title=f"Guess the State {len(states_check_list)}/50", prompt="Enter a State Name").title()
    print(user_answer)

    states_file = pd.read_csv("50_states.csv")
    for state in states_file["state"]:
        # print(states)
        if state == user_answer and user_answer not in states_check_list:
            print("Got one!")
            states_check_list.append(user_answer)
            correct_state = states_file[states_file["state"] == state]
            name_state.write_state_name(user_answer, float(correct_state["x"]), float(correct_state["y"]))
            print(correct_state["state"])
            # print(state_pos)

        if len(states_check_list) >= 50:
            print("You got all of them!")
            game_on = False
            break

        if user_answer == "Exit":
            game_on = False
            # missing_states = []
            # for state in states_file["state"]:
            #     if state not in states_check_list:
            #         missing_states.append(state)

            # Using List Comprehension from next day lesson
            missing_states = [states for states in states_file["state"] if states not in states_check_list]

            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv("states_to_learn.csv")


    # print(states_check_list)
print(f"Your final score is {len(states_check_list)}/50")

turtle.mainloop()
# game_screen.exitonclick()