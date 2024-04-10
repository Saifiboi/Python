from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_array = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if (random.randint(1, 6)) == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            y_ran = -240 + (random.randint(0, 19) * 25)
            if y_ran == 235:
                y_ran += 15
            new_car.goto(300, y_ran)
            for i in self.car_array:
                if new_car.distance(i) < 50:
                    new_car.goto(x=50 + new_car.distance(i) + 300, y=y_ran)
                    break
            self.car_array.append(new_car)

    def move(self):
        for i in self.car_array:
            i.backward(self.car_speed)

    def inc_speed(self):
        self.car_speed += MOVE_INCREMENT
