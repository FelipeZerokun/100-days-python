from tkinter import *
window = Tk()
window.title("My first GUI program")
window.minsize(width=600, height=500)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack(expand= True)

my_label["text"] = "New Text"
my_label.config(text= "New Text")

# Button
def button_pressed():
    print("Button pressed!")
    my_label.config(text=input.get())

button = Button(text= "Click me", command= button_pressed)
button.pack()

# Entry
input = Entry(width = 10)
input.pack()

# Text
text = Text(height= 5, width= 30)
# Puts cursor in textbox
text.focus()
# Adds some text to begin with
text.insert(END, "Example of multi-line text entry")
# Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

# Spinbox
def spinbox_used():
    # gets the current value in spinbox
    print(spinbox.get())

spinbox = Spinbox(from_ = 0, to=10, width= 5, command= spinbox_used)
spinbox.pack()

# Scale
# Called with current scale value
def scale_used(value):
    print(value)

scale = Scale(from_=0, to=100, command= scale_used)
scale.pack()

# CheckButton
def checkbutton_used():
    # prints 1 if On Button checked, otherwise 0
    print(checked_state.get())

checked_state = IntVar()
checkbutton =  Checkbutton(text="Is on?",
                           variable=checked_state,
                           command=checkbutton_used)
checked_state.get()
checkbutton.pack()

# RadioButton
def radio_used():
    print(radio_state.get())

radio_state = IntVar()
radiobutton1 = Radiobutton(text= "Option1",
                           value=1,
                           variable= radio_state,
                           command= radio_used)

radiobutton2 = Radiobutton(text= "Option2",
                           value=2,
                           variable= radio_state,
                           command= radio_used)

radiobutton1.pack()
radiobutton2.pack()

# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height= 4)
fruits = ["Apple", "Pear", "Tangerine", "Orange"]
for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()



window.mainloop()