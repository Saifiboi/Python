from tkinter import *
from time import sleep
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
my_window = Tk()
my_window.config(bg=BACKGROUND_COLOR)
my_window.config(padx=50, pady=50)
my_window.title("Flashy")
my_canvas = Canvas()
try:
    my_panda = pandas.read_csv(filepath_or_buffer="./data/remaining_words.csv")
except FileNotFoundError:
    my_panda = pandas.read_csv(filepath_or_buffer="./data/french_words.csv")
my_french = my_panda['French'].tolist()
my_english = my_panda['English'].tolist()
print(len(my_french))
index = random.randint(0, len(my_french) - 1)

my_canvas.config(width=800, height=530)
my_canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
card_photo_front = PhotoImage(file="./images/card_front.png")
card_photo_back = PhotoImage(file="./images/card_back.png")
my_pic = my_canvas.create_image(0, 0, image=card_photo_front, anchor="nw")
my_title = my_canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
my_data = my_canvas.create_text(400, 263, text=f"{my_french[index]}", font=("Ariel", 60, "bold"))


def update_db():
    my_french.pop(index)
    my_english.pop(index)
    df = pandas.DataFrame(zip(my_french, my_english), columns=['French', 'English'])
    df.to_csv("./data/remaining_words.csv")
    next_card()


def flip_cards():
    my_canvas.itemconfig(my_pic, image=card_photo_back)
    my_canvas.itemconfig(my_title, text="English", fill="white")
    my_canvas.itemconfig(my_data, text=f"{my_english[index]}", fill="white")


my_timer = my_window.after(3000, func=flip_cards)


def next_card():
    global index, my_timer
    my_window.after_cancel(my_timer)
    index = random.randint(0, len(my_french) - 1)
    my_canvas.itemconfig(my_pic, image=card_photo_front)
    my_canvas.itemconfig(my_title, text="French", fill="black")
    my_canvas.itemconfig(my_data, text=f"{my_french[index]}", fill="black")
    my_timer = my_window.after(3000, func=flip_cards)


my_canvas.grid(row=0, column=0, columnspan=2)
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_img, command=next_card)
wrong_btn.config(highlightthickness=0)
wrong_btn.grid(row=1, column=0)
right_img = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, command=update_db)
right_btn.grid(row=1, column=1)
next_card()
my_window.mainloop()
