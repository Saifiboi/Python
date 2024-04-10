from tkinter import *
from functools import partial
from quiz_brain import QuizBrain
import timer

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quizer: QuizBrain):
        self.tim = None
        self.quiz = quizer
        self.count = 300
        global THEME_COLOR
        self.window = Tk()
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = Label()
        self.score.config(text="Score:0", bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1)
        self.timer = Label()
        self.timer.config(text="00:00", bg=THEME_COLOR, fg="white")
        self.timer.grid(row=0, column=0)
        self.canv = Canvas()
        self.canv.config(height=250, width=300)
        self.text = self.canv.create_text(150, 125, text="Questions are going to appear in 10 seconds.",
                                          fill=THEME_COLOR, font=("Ariel", 20, "italic"), width=280)
        self.canv.grid(row=1, column=0, columnspan=2, pady=50)
        r_image = PhotoImage(file="./images/true.png")
        self.button_r = Button(image=r_image, highlightthickness=0, command=partial(self.Question_check, "True"))
        self.button_r.grid(row=2, column=0)
        l_image = PhotoImage(file="./images/false.png")
        self.button_l = Button(image=l_image, highlightthickness=0, command=partial(self.Question_check, "False"))
        self.button_l.grid(row=2, column=1)
        self.button_l.config(state="disabled")
        self.button_r.config(state="disabled")
        self.s = self.window.after(10000, self.start_quiz)
        self.window.mainloop()

    def start_quiz(self):
        self.window.after_cancel(self.s)
        txt = self.quiz.next_question()
        self.canv.itemconfig(self.text, text=txt)
        self.button_l.config(state="active")
        self.button_r.config(state="active")
        while self.count > 0:
            self.tim = self.window.after(1000, partial(timer.count_down, self.count, self.timer))
            self.count -= 1
        self.Question_check("false")

    def Question_check(self, arg):
        self.window.after_cancel(self.tim)
        self.count = 300
        res, corr = self.quiz.check_answer(arg)
        if corr:
            self.canv.config(bg="green")
        else:
            self.canv.config(bg="red")
        self.window.after(1000, self.rev)
        self.score.config(text=f"Score:{res}")

    def rev(self):
        self.count = 300
        self.canv.config(bg="white")
        try:
            txt = self.quiz.next_question()
            self.canv.itemconfig(self.text, text=txt)
            while self.count > 0:
                self.tim = self.window.after(1000, partial(timer.count_down, self.count, self.timer))
                self.count -= 1
                self.Question_check("false")
        except ValueError:
            self.canv.itemconfig(self.text, text=f"Quiz Completed. Score{self.quiz.score}/{self.quiz.question_number}\
             !Window will be destroyed in 10 seconds.")
            self.button_l.config(state="disabled")
            self.button_r.config(state="disabled")
            self.window.after(10000, self.window.destroy)
