import time
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_obj = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer_obj)
    timer_label.config(text="timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        print("Long Break")
        timer_label.config(text="Long break", fg=RED)
        timer = LONG_BREAK_MIN*60
        reps = 0

    elif reps % 2 == 0:
        print("Short break")
        timer_label.config(text="Short break", fg=PINK)
        timer = SHORT_BREAK_MIN*60

    else:
        print("Working time")
        timer_label.config(text="Working time", fg=GREEN)
        timer = WORK_MIN*60

    count_down(timer)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    # time format 00:00
    minutes = int(count/60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if count >= 0:
        global timer_obj
        timer_obj = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = int(reps/2)
        for _ in range(work_sessions):
            marks += '✔'
        print(marks)
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width= 380, height= 224, bg= YELLOW, highlightthickness= 0) # Same to the Image size
tomato_image = PhotoImage(file="tomato.png")

canvas.create_image(190, 112, image=tomato_image)
timer_text = canvas.create_text(190, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)


# Timer Label
timer_label = Label(text="Timer", bg= YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)

# Buttons
start_button = Button(text="start", highlightthickness= 0, command= start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="reset", highlightthickness= 0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Check marks
check_marks = Label(bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
