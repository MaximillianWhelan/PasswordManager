from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json

PURPLE = "#48426d"

# ---------------------------- SEARCH FOR WEBSITE ------------------------------- #


def search_for_website():
    email = "email"
    password = "password"
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            website_name = data[website_entry.get()]
    except KeyError:
        messagebox.showinfo(title="Oops", message="There was no website with this name in the database.")
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="There was no file available to search")
    else:
        messagebox.showinfo(title="Credentials", message=f"Your email address is: {website_name[email]} "
                                                         f"and your password is: {website_name[password]}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_to_txt():

    new_data = {
        website_entry.get(): {
            "email": email_entry.get(),
            "password": password_entry.get()
        }
    }

    if len(website_entry.get()) == 0 or len(email_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(title="Warning", message="Please don't leave any fields blank.")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Creating a window
window = Tk()
window.title("My Password Manager")
window.config(pady=50, padx=50, bg=PURPLE)
window.resizable(False, False)

# Creating a canvas
canvas = Canvas(height=200, width=189, bg=PURPLE, highlightthickness=0)
pass_lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_lock_image)
canvas.grid(column=1, row=0)

# Creating labels
website_label = Label(text="Website:", bg=PURPLE, fg="white")
website_label.grid(column=0, row=1, pady=(0, 10))
email_label = Label(text="Email/Username:", bg=PURPLE, fg="white")
email_label.grid(column=0, row=2, pady=(0, 10))
password_label = Label(text="Password:", bg=PURPLE, fg="white")
password_label.grid(column=0, row=3, pady=(0, 10))

# Entries
website_entry = Entry()
website_entry.grid(column=1, row=1, sticky="EW", pady=(0, 10), ipady=3, padx=(0, 10))
website_entry.focus()
email_entry = Entry()
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW", ipady=4, pady=(0, 10))
password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="EW", ipady=4, padx=(0, 10))


# Buttons
generate_password = Button(text="Generate Password", command=gen_password)
generate_password.grid(row=3, column=2, sticky="W", ipady=1, pady=2, ipadx=3)
add_button = Button(text="Add", width=30, command=save_to_txt)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW", ipady=2, pady=10)
search_button = Button(text="Search", command=search_for_website)
search_button.grid(row=1, column=2, sticky="NW", ipadx=35)

window.mainloop()
