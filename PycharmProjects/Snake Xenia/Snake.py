from turtle import Screen, Turtle
from random import randint
from time import *
from threading import Thread

MOVEDISTANCE = 20
headstart = [0, 0]


class Snake:
    def __init__(self):
        self.length = 3
        self.last_x = 0
        self.last_y = -40
        self.turtle_array = []
        self.start_snake()

    def start_snake(self):
        for i in range(0, self.length):
            self.turtle_array.append(Turtle(shape="square"))
            self.turtle_array[i].penup()
            self.turtle_array[i].color("white")
            self.turtle_array[i].goto(-20 * i + headstart[0], headstart[1])
            self.turtle_array[0].shape("triangle")

    def move_snake(self):

        i = 1
        for turtle_num in range(len(self.turtle_array) - 1, 0, -1):
            self.turtle_array[turtle_num].goto(self.turtle_array[turtle_num - 1].xcor(),
                                               self.turtle_array[turtle_num - 1].ycor())
            i += 1
        if self.xcord() + MOVEDISTANCE > 300:
            self.turtle_array[0].forward(300 - self.xcord())
        elif self.xcord() - MOVEDISTANCE < -305:
            self.turtle_array[0].forward(305 + self.xcord())
        elif self.ycord() + MOVEDISTANCE > 285:
            self.turtle_array[0].forward(285 - self.ycord())
        elif self.ycord() - MOVEDISTANCE < -285:
            self.turtle_array[0].forward(285 + self.ycord())
        else:
            self.turtle_array[0].forward(MOVEDISTANCE)
        headstart[0] = self.turtle_array[0].xcor()
        headstart[1] = self.turtle_array[1].ycor()
        sleep(0.1)

    def up(self):
        if self.turtle_array[0].heading() != 270:
            self.turtle_array[0].setheading(90)
        self.move_snake()

    def down(self):
        if self.turtle_array[0].heading() != 90:
            self.turtle_array[0].setheading(270)
        self.move_snake()

    def right(self):
        if self.turtle_array[0].heading() != 180:
            self.turtle_array[0].setheading(0)
        self.move_snake()

    def left(self):
        if self.turtle_array[0].heading() != 0:
            self.turtle_array[0].setheading(180)
        self.move_snake()

    def distance(self, arg):
        return self.turtle_array[0].distance(arg, y=None)

    def inc_size(self):
        self.length += 1
        self.turtle_array.append(Turtle(shape="square"))
        self.turtle_array[self.length - 1].hideturtle()
        self.turtle_array[self.length - 1].color("white")
        self.turtle_array[self.length - 1].penup()
        self.turtle_array[self.length - 1].goto(-MOVEDISTANCE * self.length - 1 + headstart[0], headstart[1])
        self.turtle_array[self.length - 1].showturtle()

    def xcord(self):
        return self.turtle_array[0].xcor()

    def ycord(self):
        return self.turtle_array[0].ycor()

    def game_check(self):
        live = True
        for i in range(1, len(self.turtle_array)):
            if self.turtle_array[0].distance(self.turtle_array[i]) < 70:
                live = False
            else:
                live = True
        return live
