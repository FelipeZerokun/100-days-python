from tkinter import *
from kanji_database import kanji_list, kanji_dataset
from random import choice
import pandas as pd

# -------------------------- Creating words for the cards -------------------------- #


def new_word():
    global kanji_list, kanji_word, english_meaning, flip_timer
    game_window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image=card_front)
    kanji_word = choice(kanji_list)
    word_characteristics = kanji_dataset[kanji_word]
    english_meaning = word_characteristics["wk_meanings"]
    on_readings = word_characteristics["wk_readings_on"]
    kun_readings = word_characteristics["wk_readings_kun"]
    canvas.itemconfig(canvas_text, text=kanji_word, fill='black')
    canvas.itemconfig(canvas_language, text="Japanese", fill='black')
    canvas.itemconfig(canvas_on_reading, text=on_readings, fill='black')
    canvas.itemconfig(canvas_kun_reading, text=kun_readings, fill='black')

    if len(kanji_list) > 0:
        flip_timer = game_window.after(3000, flip_card)
    # print(english_meaning)


# ------------------------------------ Game structure ------------------------------------ #


def flip_card():
    global english_meaning
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(canvas_text, text=english_meaning, fill='white')
    canvas.itemconfig(canvas_language, text="English", fill='white')
    canvas.itemconfig(canvas_on_reading, text="")
    canvas.itemconfig(canvas_kun_reading, text="")

def known_word():
    global kanji_list, kanji_word
    print(kanji_word)
    kanji_list.remove(kanji_word)
    data = pd.DataFrame(kanji_list)
    data.to_csv("data/kanjis_to_learn.csv")
    new_word()

# ------------------------------------ Creating the UI ------------------------------------ #


BG_COLOR = '#B1DDC6'
kanji_word = choice(kanji_list)
word_characteristics = kanji_dataset[kanji_word]
english_meaning = word_characteristics["wk_meanings"]
on_readings = word_characteristics["wk_readings_on"]
kun_readings = word_characteristics["wk_readings_kun"]

game_window = Tk()
game_window.minsize(width=900, height=600)
game_window.config(padx=50, pady=50, background=BG_COLOR)
flip_timer = game_window.after(3000, flip_card)

# First, loading the images
card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

# Now, let's create the cards with canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, background=BG_COLOR)
canvas_image = canvas.create_image(400, 263, image=card_front)
canvas_language = canvas.create_text(400, 150, fill='black', font=('Ariel', 35, 'italic'), text="Japanese")
canvas_text = canvas.create_text(400, 263, fill='black', font=('Ariel', 35, 'bold'), text= kanji_word)
canvas_on_reading = canvas.create_text(300, 350, fill='black', font=('Ariel', 25, 'bold'), text= on_readings)
canvas_kun_reading = canvas.create_text(500, 350, fill='black', font=('Ariel', 25, 'bold'), text= kun_readings)
canvas.grid(row=0, column=0, columnspan=2)

# Finally, let's create the buttons
right_button = Button(image=right_image, height=100, width=100, highlightthickness=0, command=known_word)
right_button.grid(row=1, column=1)

wrong_button = Button(image=wrong_image, height=100, width=100, highlightthickness=0, command=new_word)
wrong_button.grid(row=1, column=0)


game_window.mainloop()
