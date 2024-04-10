from turtle import Turtle


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.pendown()
        self.setheading(270)
        self.pensize(5)
        while self.ycor() > -280:
            self.pendown()
            self.forward(15)
            self.penup()
            self.forward(15)

    def game_start(self):
        self.penup()
        self.goto(0, -50)
        self.write("Click to start", align="center", font=("Courier", 30, 'normal'))

    def game_over(self):
        self.penup()
        self.goto(0, -50)
        self.write("Game  Over!!", align="center", font=("Courier", 30, 'normal'))
