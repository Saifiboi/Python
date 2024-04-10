# from tkinter import *
#
# window = Tk()
# window.minsize(500, 500)
# my_label = Label(text="New input")
# my_label.grid(column=0, row=0)
# my_entry = Entry(width=10)
# my_entry.grid(column=3, row=2)
#
#
# def btn_clicked():
#     my_label["text"] = my_entry.get()
#
#
# my_button = Button(text="Click ME!", command=btn_clicked)
# my_button.grid(column=1, row=1)
#
# new_btn = Button(text="New Button!")
# new_btn.grid(column=2, row=0)
# window.mainloop()
from tkinter import *

window = Tk()
window.title("Miles to Kilometers")
window.config(padx=20, pady=20)
window.minsize(300, 100)
my_entry = Entry(width=10)
my_entry.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 15, "normal"))
miles_label.grid(column=2, row=0)

makes_label = Label(text="Makes", font=("Arial", 10, "normal"))
makes_label.grid(column=0, row=2)

var = 0
var_label = Label(text=var, font=("Arial", 20, "normal"))
var_label.grid(column=1, row=2)

kilometers_label = Label(text="Kilometers", font=("Arial", 15, "normal"))
kilometers_label.grid(column=2, row=2)


def btn_click():
    global var
    var = int(my_entry.get())
    var_label.config(text=var * 1.6)


new_btn = Button(text="Calculate", command=btn_click)
new_btn.grid(column=1, row=3)
window.mainloop()
