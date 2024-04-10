from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("#999900")
        self.penup()
        self.shape("circle")
        self.goto(randint(-280,280), randint(-260, 260))
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)

    def reallocate(self):
        self.goto(randint(-280, 280), randint(-260, 260))
