import tkinter
from tkinter import messagebox
import random
import pyperclip


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
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't Left any fields empty.")
        return 0

    is_ok = messagebox.showinfo(title="Title",
                                message=f"These are the details entered:\nWebsite: {website} \nEmail: {email} \nPassword: {password} \n Is it OK to save?")

    if is_ok:
        messagebox.showinfo(title="Password Saved", message="Password Copied to clipboard. ")
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")

        website_entry.delete(0, 25)
        password_entry.delete(0, 25)
        email_entry.delete(0, 25)
    else:
        return 0


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
website_entry = tkinter.Entry(width=40)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = tkinter.Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = tkinter.Entry(width=22)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = tkinter.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = tkinter.Button(text="Add", width=33, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()