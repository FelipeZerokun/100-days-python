from tkinter import *

############################ MY CONSTANTS ############################
FONT = ("Arial", 12, "bold")


############################ MY FUNCTIONS ############################


def button_pressed():
    print("Button pressed!")
    unit_conv = conversion(user_input.get())
    result_label.config(text=unit_conv)


def conversion(measure):
    return round(int(measure)*1.60934, 1)

############################ MAIN PROGRAM ############################


window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=290, height=125)
window.config(padx=20, pady=20)

# Miles label
miles_label = Label(text="miles", font=FONT)
miles_label.grid(column=3, row=0)

# KM label
KM_label = Label(text="KM", font=FONT)
KM_label.grid(column=3, row=2)

# Is equal to label
is_equal_to_label = Label(text= "is equal to", font= FONT)
is_equal_to_label.grid(column=1, row=1)

# Result label
result_label = Label(text= "0", font=FONT)
result_label.grid(column=2, row=1)

# Data entry
user_input = Entry(width= 12)
user_input.grid(column=2, row=0)

# Calculate button
calculate_button = Button(text= "Calculate", width=12, command=button_pressed)
calculate_button.grid(column=2, row=2)



window.mainloop()