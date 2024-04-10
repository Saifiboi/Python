from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = ""


# ---------------------------- TIMER RESET ------------------------------- #
def reset_time():
    global timer
    windows.after_cancel(timer)
    my_canvas.itemconfig(can_text, text="00:00")
    Timer_label.config(text="Timer", fg=GREEN)
    tick_mark.config(text="")


# ---------------------------- UI SETUP ------------------------------- #

    else:
        tick_txt = ""
        if reps == 1:
            tick_txt = "tick"
        else:
            for i in range(1, int(reps / 2) + 2, 2):
                tick_txt = tick_txt + "tick"
        tick_mark.config(text=tick_txt)
        start_countdown()


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_countdown():
    global reps
    if reps % 2 == 1:
        Timer_label.config(text="WORK", fg=GREEN)
        count_down(WORK_MIN * 60)
    elif reps == 8:
        Timer_label.config(text="LONG BREAK", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    else:
        Timer_label.config(text="SHORT BREAK", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)

    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
windows = Tk()
windows.title("Pomodoro")
windows.config(padx=100, pady=100, bg=YELLOW)
Timer_label = Label(text="TIMER", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
Timer_label.grid(column=1, row=0)
tomato = PhotoImage(file="../Stop Watch/tomato.png")
my_canvas = Canvas(width=220, height=223, bg=YELLOW, highlightthickness=0)
my_canvas.create_image(103, 110, image=tomato)
can_text = my_canvas.create_text(103, 124, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
my_canvas.grid(column=1, row=1)
start_btn = Button(text="Start", width=5, bg="white", highlightthickness=0, command=start_countdown)
start_btn.grid(column=0, row=2)
tick_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
tick_mark.grid(column=1, row=3)
stop_btn = Button(text="Stop", width=5, bg="white", highlightthickness=0, command=reset_time)
stop_btn.grid(column=2, row=2)
windows.mainloop()
