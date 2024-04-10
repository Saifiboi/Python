from turtle import Screen, Turtle
from random import randint
from Snake import Snake
from time import *
from food import Food
from scoreboard import ScoreBoard
from threading import Thread

my_screen = Screen()
my_screen.setup(width=600, height=550)
my_screen.title("Snake Xenia")
my_screen.tracer(0)


def change_background():
    color = ["black", "#66ff99", "blue", "#ff4d4d"]
    prev = -1
    new = randint(0, 12) % 4
    while new == prev:
        new = randint(0, 12) % 4
    my_screen.bgcolor(color[new])
    prev = new


turtle_array = []

my_screen.ontimer(fun=change_background, t=1)
my_snake = Snake()
my_food = Food()
my_scoreboard = ScoreBoard()
my_screen.update()
my_screen.listen()
my_screen.onkey(key="Up", fun=my_snake.up)
my_screen.onkey(key="Down", fun=my_snake.down)
my_screen.onkey(key="Right", fun=my_snake.right)
my_screen.onkey(key="Left", fun=my_snake.left)
while 1:
    my_screen.update()
    sleep(0.1)
    my_snake.move_snake()
    y_cor_check = my_snake.ycord() > -270 or my_snake.ycord() < 270
    x_cor_check = my_snake.xcord() > -300 or my_snake.xcord() < 300
    if my_snake.distance(my_food) < 18:
        my_food.reallocate()
        my_scoreboard.update_score()
        my_snake.inc_size()
    # if ((my_snake.xcord() >= 300 or my_snake.xcord() <= -305)and y_cor_check) or ((my_snake.ycord() >= 285 or my_snake.ycord() <= -280) and x_cor_check):
    #     my_scoreboard.game_over()
    #     break
    if my_snake.game_check():
        break

my_screen.exitonclick()
