from turtle import Turtle as Tt, Screen as Ss
import turtle
from random import uniform, randint


def rand_col():
    my_tuple = (randint(0, 255), randint(0, 255), randint(0, 255))
    return my_tuple

def draw_strgnograph(size):
    my_turtle = Tt()
    my_screen = Ss()
    turtle.colormode(255)
    my_turtle.shape("turtle")
    my_turtle.color("yellow4")
    my_turtle.speed(0)
    my_turtle.pensize(2)
    for i in range(int(360/size)):
        my_turtle.pencolor(rand_col())
        my_turtle.circle(100)
        curr = my_turtle.heading()
        my_turtle.setheading(curr+size)
    my_screen.exitonclick()
draw_strgnograph(10)
# for i in range(300):
#         my_tuple = ([randint(0, 255), randint(0, 255), randint(0, 255)])
#         my_turtle.pencolor(my_tuple)
#         my_turtle.forward(10)
#         if randint(0, 10)%2==0:
#             my_turtle.right(90)
#         else:
#             my_turtle.left(90)
#
