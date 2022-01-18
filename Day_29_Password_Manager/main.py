from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
# import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# C ode from my day 05 project: Password Generator


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_entry.delete(0, END) # Clear the password Entry

    password_letters = [choice(letters) for _ in range(randint(5, 7))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 5))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 5))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    print(password)
    password_entry.insert(0, password)
    # pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    # print("Data saved")
    website = website_entry.get().strip()
    email_username = email_username_entry.get().strip()
    password = password_entry.get().strip()

    if website == "" or email_username == "" or password == "":
        messagebox.showwarning(title="Saving password...", message="Don't leave any entry empty!")

    else:
        user_OK = messagebox.askyesno(title="Saving password...", message="Are you sure this is OK?")

        if user_OK:
            with open("data.txt", "a") as file:
                file.write(f"{website}  |  {email_username}  |  {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

            messagebox.showinfo(title="Saving password...", message="Password saved successfully")

        else:
            messagebox.showinfo(title="Saving password...", message="The password was not saved")

# ---------------------------- UI SETUP ------------------------------- #


main_window = Tk()

main_window.title("Password Generator")
main_window.config(padx=50, pady=50)

canvas = Canvas(width= 200, height= 200) # Same to the Image size
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

# Creating the labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Creating the Entries

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()

email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_username_entry.insert(0, "yourmail@example.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="EW")

# Creating the buttons
generate_pass_button = Button(text= "Generate Password", command=generate_password)
generate_pass_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text= "Add", width= 36, command= save)
add_button.grid(column=1, row=4, columnspan=2)


main_window.mainloop()
