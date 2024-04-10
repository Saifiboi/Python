# import colorgram
from turtle import Turtle as Tt, Screen as Ss
import turtle
import random

# rgb_color=[]
# colors = colorgram.extract('paint.jpg', 15)
color_list = [(239, 221, 113), (18, 111, 193), (223, 60, 95), (235, 150, 76), (18, 111, 193), (116, 147, 208),
              (143, 88, 50), (212, 127, 164), (34, 194, 117)]
# for color in colors:
#     rgb_color.append((color.rgb.r,color.rgb.g,color.rgb.b))
# print(rgb_color)
my_turtle = Tt()
turtle.colormode(255)
my_turtle.shape("turtle")
my_turtle.color("Red")
my_turtle.speed(0)
my_turtle.pensize(2)
my_turtle.penup()
my_turtle.hideturtle()
start_x = -300
start_y = -240
my_screen = Ss()
my_screen.screensize(10, 10, "pink")
my_turtle.setx(start_x)
my_turtle.sety(start_y)
for j in range(10):
    for i in range(10):
        color = random.choice(color_list)
        my_turtle.dot(20, color)
        my_turtle.forward(50)
    my_turtle.setx(start_x)
    my_turtle.sety(start_y + 50)
    start_y += 50

my_screen.exitonclick()
