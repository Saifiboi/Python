from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.shape("turtle")
        self.color("black")

    def move(self):
        if self.ycor()+MOVE_DISTANCE <= 290:
            self.forward(MOVE_DISTANCE)
        else:
            self.forward(290-(self.ycor()))

    def r_move(self):
        if self.xcor() + MOVE_DISTANCE <= 280:
            self.goto(y=self.ycor(), x=self.xcor() + MOVE_DISTANCE)

    def l_move(self):
        if self.xcor() + MOVE_DISTANCE >= -270:
            self.goto(y=self.ycor(), x=self.xcor() - MOVE_DISTANCE)

    def b_move(self):
        if self.ycor() - MOVE_DISTANCE >= -280:
            self.back(MOVE_DISTANCE)
