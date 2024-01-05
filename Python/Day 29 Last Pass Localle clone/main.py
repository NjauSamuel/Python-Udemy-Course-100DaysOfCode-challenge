import tkinter
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Password Generator Project

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email_or_username = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email_or_username": email_or_username,
            "password" : password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't Left any fields empty.")
        return 0

    is_ok = messagebox.showinfo(title="Title",
                                message=f"These are the details entered:\nWebsite: {website} \nEmail/UserName: {email_or_username} \nPassword: {password} \n Is it OK to save?")

    if is_ok:
        messagebox.showinfo(title="Password Saved", message="Password Copied to clipboard. ")
        try:
            with open("data.json", "r") as data_file:

                # Reading the old data.
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating the old data with the new data.
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving Updated data.
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, 25)
            password_entry.delete(0, 25)
            email_entry.delete(0, 25)
    else:
        return 0


# ---------------------------- Find Password ------------------------------- #

def find_password():
    website = website_entry.get()

    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
            print(data)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data file found")
    else:
        if website in data:
            email = data[website]["email_or_username"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists. ")


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = tkinter.Canvas(width=200, height=200)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = tkinter.Label(text="Website")
website_label.grid(row=1, column=0)
email_label = tkinter.Label(text="Email/Username")
email_label.grid(row=2, column=0)
password_label = tkinter.Label(text="Password")
password_label.grid(row=3, column=0)

# Entries
website_entry = tkinter.Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = tkinter.Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = tkinter.Entry(width=22)
password_entry.grid(row=3, column=1)

# Buttons
search_button = tkinter.Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2)
generate_password_button = tkinter.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = tkinter.Button(text="Add", width=33, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
