import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Code from my day 05 project: Password Generator


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
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    # print("Data saved")
    website = website_entry.get().strip().title()
    email_username = email_username_entry.get().strip()
    password = password_entry.get().strip()
    # json dictionary format
    new_data = {
        website: {
            "email": email_username,
            "password": password
        }
    }

    if len(website) == 0 or len(email_username) == 0 or len(password) == 0:
        messagebox.showwarning(title="Saving password...", message="Don't leave any entry empty!")

    else:
        try:
            # We are going to use JSON data structure
            with open("data.json", "r") as file:
                # Writing in json format (needs "w" mode)
                # json.dump(new_data, file, indent=4)

                # Reading in json format (needs "r" mode)
                # data = json.load(file)  # this is a python dictionary
                # print(data)

                # Updating in json format (needs both "w" and "r" mode)
                data = json.load(file)  # First, we must open the file

        except:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent= 4)

        else:
            data.update(new_data)  # Now, we create a new structure with the updated data
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4) #finally, we write all the new data into the file

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

        messagebox.showinfo(title="Saving password...", message="Password saved successfully")

# ---------------------------- SEARCH FUNCTION ------------------------------- #


def search():
    website_keyword = website_entry.get().title()
    try:
        with open("data.json", "r") as file:
            data_dict = json.load(file)
            print(data_dict)

    except:
        messagebox.showwarning(title="File not found", message="First, you need to save some data!")

    else:
        try:
            data_found = data_dict[website_keyword]

        except KeyError:
            messagebox.showwarning(title="Page not found", message=f"There is no data of '{website_keyword}' page")

        else:
            messagebox.showinfo(title= f"{website_keyword} page", message=f'email: {data_found["email"]}\n'
                                                                          f'Password: {data_found["password"]}')
            pyperclip.copy(data_found["password"])


    finally:
        website_entry.delete(0, END)



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

website_entry = Entry(width=33)
website_entry.grid(column=1, row=1, columnspan=2, sticky="W")
website_entry.focus()

email_username_entry = Entry(width=51)
email_username_entry.grid(column=1, row=2, columnspan=2, sticky="W")
email_username_entry.insert(0, "randomemailaddres@hotmail.com")

password_entry = Entry(width=33)
password_entry.grid(column=1, row=3, sticky="W")

# Creating the buttons
generate_pass_button = Button(text= "Generate Password", width=14 , command=generate_password)
generate_pass_button.grid(column=2, row=3)

add_button = Button(text= "Add", width= 36, command= save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=14, command= search)
search_button.grid(column=2, row=1)
main_window.mainloop()