from tkinter import *
from tkinter import messagebox
import random
# import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_pass():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for i in range(nr_letters)]
    password_list.extend([random.choice(numbers) for j in range(nr_numbers)])
    password_list.extend([random.choice(symbols) for k in range(nr_symbols)])
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(string=password, index=0)
    # pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    check = False
    prev_data = {}
    web_name = website_entry.get()
    user_name = Username_entry.get()
    password = password_entry.get()
    if len(web_name) == 0:
        messagebox.showerror(title="Invalid Entry", message="Website Field can't be none. ")
        check = True
    if len(password) == 0 and not check:
        messagebox.showerror(title="Invalid Entry", message="Password Field can't be none. ")
        check = True
    if len(user_name) == 10 and not check:
        messagebox.showerror(title="Invalid Entry", message="Please Enter a valid email address. ")
        check = True
    if not check:
        res = messagebox.askokcancel(title=web_name, message=f"Email :{user_name}\nPassword : {password}\nIs it okay?")
        data_dict = {
            web_name:
                {"Email": user_name,
                 "password": password}
        }
        if res:
            try:
                with open("data.json", mode='r') as file:
                    prev_data = json.load(file)
                    prev_data.update(data_dict)
            except FileNotFoundError:
                prev_data = data_dict
            finally:
                with open("data.json", mode='w') as file:
                    json.dump(prev_data, file, indent=4)
                    website_entry.delete(0, END)
                    Username_entry.delete(0, END)
                    Username_entry.insert(END, "@gmail.com")
                    website_entry.focus()
                    password_entry.delete(0, END)


# ---------------------------- Search Password ------------------------------- #
def search_pass():
    try:
        with open("data.json", mode='r') as file:
            prev_data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="File does not exist. ")
    else:
        website_name = website_entry.get()
        new_dict = {}
        try:
            new_dict = prev_data[website_name]
        except KeyError:
            messagebox.showerror(title="Error", message=f"{website_name}'s password is not saved yet . ")
        else:
            email = new_dict["Email"]
            passw = new_dict["password"]
            messagebox.showinfo(title=website_name, message=f"The Email:{email}\nPassword:{passw}" )
    finally:
        website_entry.delete(0, END)
        Username_entry.delete(0, END)
        Username_entry.insert(END, "@gmail.com")
        website_entry.focus()
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------#
windows = Tk()
windows.title("Password Generate")
windows.config(padx=40, pady=40)
my_canvas = Canvas(width=200, height=200, highlightthickness=0)
lock = PhotoImage(file="logo.png")
my_canvas.create_image(100, 100, image=lock)
my_canvas.grid(row=0, column=1)
website_label = Label(text="Website:", fg="black", font=("Courier", 10, "normal"))
website_label.grid(row=1, column=0)
website_entry = Entry(width=32)
website_entry.focus()
website_entry.grid(row=1, column=1)
Username_label = Label(text="Email/Username:", fg="black", font=("Courier", 10, "normal"))
Username_label.grid(row=2, column=0)
Username_entry = Entry(width=52)
Username_entry.insert(END, "@gmail.com")
Username_entry.grid(row=2, column=1, columnspan=2)
password_label = Label(text="Password:", fg="black", font=("Courier", 10, "normal"))
password_label.grid(row=3, column=0)
password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)
password_btn = Button(text="Generate Password", width=15, command=generate_pass)
password_btn.grid(row=3, column=2)
Add_btn = Button(text="Add", width=44)
Add_btn.config(command=save)
Add_btn.grid(row=4, column=1, columnspan=2)
search_btn = Button(text="Search", width=15, command=search_pass)
search_btn.grid(row=1, column=2)

windows.mainloop()
