from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = ''.join(password_list)
    if len(pass_form.get()) == 0:
        pass_form.insert(END, password)
        pyperclip.copy(password)
    else:
        pass_form.delete(0,END)
        pass_form.insert(END, password)
        pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = web_form.get()
    email = email_form.get()
    password = pass_form.get()
    new_dict = {
        web.lower() : {
            "email" : email.lower(),
            "password" : password.lower()
        }
    }
    
    if len(web) <= 0 or len(email) <= 0 or len(password) <= 0:
        messagebox.showinfo(title="Warning", message="Your data is incomplete")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_dict, data_file, indent=4)
        else:
            data.update(new_dict)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_form.delete(0,END)
            email_form.delete(0,END)
            pass_form.delete(0,END)
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    web = web_form.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Not Found", message="Data is not found")
    else:
        try:
            mail = data[web]["email"]
            this_pass = data[web]["password"]
        except KeyError:
            messagebox.showinfo(title="Not Found", message="No email found")
        else:
            messagebox.showinfo(title=f"{web}", message=f"Email : {mail}\nPassword : {this_pass}")

# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()

windows.config(padx=20,pady=20)

logo_image = PhotoImage(file="logo.png")

logo = Canvas(width=200, height =200)
logo.create_image(100,100,image = logo_image)

logo.grid(column=1, row=0)

#Label
web_label = Label(text="Website:", font=("Arial", 10, "bold"))
web_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", font=("Arial", 10, "bold"))
email_label.grid(column=0, row=2)
pass_label = Label(text="Password:", font=("Arial", 10, "bold"))
pass_label.grid(column=0, row=3)

#Form
web_form = Entry(width=34)
web_form.grid(column=1, row=1)
web_form.focus()
email_form = Entry(width=53)
email_form.grid(column=1, row=2, columnspan=2)
pass_form = Entry(width=34)
pass_form.grid(column=1, row=3)

#Button
gen_pass = Button(text="Generate Password", command=generate_password, width=14)
gen_pass.grid(column=2, row=3)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)

windows.mainloop()