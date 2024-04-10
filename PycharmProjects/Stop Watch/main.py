from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
Count = 0
timer = 0


def start_countdown():
    global Count, timer
    hrs = int(Count / 3600)
    rem = Count % 3600
    mins = int(rem / 60)
    rem = rem % 60
    my_text = ""
    if hrs < 10:
        my_text = f"0{hrs}"
    else:
        my_text = f"{hrs}"
    if mins < 10:
        my_text += f":0{mins}"
    else:
        my_text += f":{mins}"
    if rem < 10:
        my_text += f":0{rem}"
    else:
        my_text += f":{rem}"
    my_canvas.itemconfig(can_text, text=my_text)
    Count += 1
    timer = windows.after(1000, start_countdown)


def stop_count():
    global timer
    windows.after_cancel(str(timer))


def reset_watch():
    global Count
    stop_count()
    my_canvas.itemconfig(can_text, text="00:00:00")
    Count = 0

windows = Tk()
windows.title("Pomodoro")
windows.config(padx=100, pady=100, bg=YELLOW)
Timer_label = Label(text="TIMER", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
Timer_label.grid(column=1, row=0)
tomato = PhotoImage(file="tomato.png")
my_canvas = Canvas(width=220, height=223, bg=YELLOW, highlightthickness=0)
my_canvas.create_image(103, 110, image=tomato)
can_text = my_canvas.create_text(103, 124, text="00:00:00", font=(FONT_NAME, 25, "bold"), fill="white")
my_canvas.grid(column=1, row=1)
start_btn = Button(text="Start", width=5, bg="white", highlightthickness=0, command=start_countdown)
start_btn.grid(column=0, row=2)
stop_btn = Button(text="Stop", width=5, bg="white", highlightthickness=0, command=stop_count)
stop_btn.grid(column=2, row=2)
reset_btn = Button(text="Reset", width=10, bg="white", highlightthickness=0, command=reset_watch)
reset_btn.grid(column=1, row=7)
windows.mainloop()
