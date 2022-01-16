from tkinter import *
window = Tk()
window.title("My first GUI program")
window.minsize(width=600, height=500)
window.config(padx=60, pady=60) #Create space between items in the screen and the window's border

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack(expand= True)

my_label["text"] = "New Text"
my_label.config(text= "New Text")
# my_label.place(x= 0, y= 0) # Upper left corner
my_label.grid(column= 0, row= 0)

# Button
def button_pressed():
    print("Button pressed!")
    my_label.config(text=input.get())

button = Button(text= "Click me", command= button_pressed)
button.grid(column= 1, row= 1)

new_button = Button(text= "A new button", command= button_pressed)
new_button.grid(column= 3, row= 0)

# Entry
input = Entry(width = 10)
input.grid(column= 3, row= 3)




window.mainloop()