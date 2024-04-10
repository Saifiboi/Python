from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, axis):
        super().__init__()
        self.shape("square")
        self.penup()
        self.setposition(x=axis, y=0)
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up_key(self):
        if self.ycor() + 10 <= 245:
            self.goto(self.xcor(), self.ycor() + 20)

    def down_key(self):
        if self.ycor() - 10 >= -245:
            self.goto(self.xcor(), self.ycor() - 20)
