from turtle import Turtle
from time import sleep


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow4")
        self.penup()
        self.x_move = 5
        self.y_move = 5
        self.timer = 0.02

    def bounce_y(self):
        self.y_move = self.y_move * -1

    def bounce_x(self):
        self.x_move = self.x_move * -1

    def reset_pos_left(self):
        self.goto(0, 0)
        self.bounce_x()

    def reset_pos_r(self):
        self.goto(0, 0)
        self.bounce_x()

    def move(self, paddle, paddle2, my_screen, my_scorebaord):
        if (self.ycor() + self.y_move > 280 or self.ycor() + self.y_move < -290) and (
                self.xcor() + self.x_move <= 380 or self.xcor() + self.x_move >= -370):
            self.bounce_y()
        if self.distance(paddle) < 50 and self.xcor() > 350:
            self.bounce_x()
            if self.x_move < 0:
                self.x_move -= 1
            else:
                self.x_move += 1
            if self.y_move < 0:
                self.y_move -= 1
            else:
                self.y_move += 1
        if self.distance(paddle2) < 50 and self.xcor() < -360:
            self.bounce_x()
            if self.x_move < 0:
                self.x_move -= 1
            else:
                self.x_move += 1
            if self.y_move < 0:
                self.y_move -= 1
            else:
                self.y_move += 1
        elif self.xcor() + self.x_move >= 380:
            my_screen.tracer(0)
            if self.x_move < 0:
                self.x_move = -5
            else:
                self.x_move = 5
            if self.y_move < 0:
                self.y_move = -5
            else:
                self.y_move = 5
            self.reset_pos_left()
            my_screen.update()
            my_scorebaord.point_left()
            sleep(1)
            my_screen.update()
            my_screen.tracer(1)
        elif self.xcor() + self.x_move < -390:
            my_screen.tracer(0)
            if self.x_move < 0:
                self.x_move = -5
            else:
                self.x_move = 5
            if self.y_move < 0:
                self.y_move = -5
            else:
                self.y_move = 5
            self.reset_pos_r()
            my_screen.update()
            my_scorebaord.point_right()
            sleep(1)
            my_screen.update()
            my_screen.tracer(1)
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)
        sleep(0.02)
