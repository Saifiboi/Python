from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-290, 260)
        self.wr()

    def wr(self):
        self.goto(-290, 260)
        self.write(arg=f"Level :{self.level}", align="left", font=FONT)

    def s_update(self):
        self.clear()
        self.level += 1
        self.wr()

    def Game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over !!", align="Center", font=FONT)
