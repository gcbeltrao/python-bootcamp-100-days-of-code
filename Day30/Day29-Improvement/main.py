from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

characters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
    "!", "@", "#", "$", "%", "&", "*", "(", ")", "-", "_", "=", "+",
    "[", "]", "{", "}", ";", ":", "'", '"', "<", ">", ",", ".", "?", "/"]


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    password_list = []
    for item in range(16):
        password_list.append(random.choice(characters))
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if website == "" or password == "":
        messagebox.showinfo(title="Missing information", message="Please do not leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered.\n Email: {email}\n"
                                                              f"Password: {password} \n It is ok to save?")
        if is_ok:
            try:
                with open("password_manager.json", "r") as password_file:
                    data = json.load(password_file)
            except (JSONDecodeError, FileNotFoundError):
                with open("password_manager.json", "w") as password_file:
                    json.dump(new_data, password_file, indent=4)
            else:
                data.update(new_data)
                with open("password_manager.json", "w") as password_file:
                    json.dump(data, password_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- SEARCH ACCOUNT ------------------------------- #
def search_account():
    account = website_entry.get()
    try:
        with open("password_manager.json", "r") as password_file:
            data = json.load(password_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Datafile found.")
    else:
        if account in data:
            email = data[account]["email"]
            password = data[account]["password"]
            messagebox.showinfo(title=account, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {account} exists.")


# ---------------------------- UI SETUP ------------------------------- #
def center_window():
    window_width = 500
    window_height = 400
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    window.geometry("+{}+{}".format(x, y))


window = Tk()
center_window()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
locker_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=locker_img)
canvas.grid(column=1, row=0)

# Website
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=32)
website_entry.focus()
website_entry.grid(column=1, row=1)

search_button = Button(text="Search", width=14, command=search_account)
search_button.grid(column=2, row=1)

# Email/Username
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=50)
email_entry.insert(0, "email@email.com")  # Put your most used email here!
email_entry.grid(column=1, row=2, columnspan=2)

# Password
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

password_button = Button(text="Generate Password", width=14, command=generate_password)
password_button.grid(column=2, row=3)

#  ADD_Button
add_button = Button(text="Add", width=43, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)
window.mainloop()
