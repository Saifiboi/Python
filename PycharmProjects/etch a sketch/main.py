# from turtle import Turtle, Screen
#
# my_turtle = Turtle()
# my_screen = Screen()
#
#
# def move_forward():
#     my_turtle.forward(10)
#
#
# def move_backward():
#     my_turtle.back(10)
#
#
# def rotate_clock():
#     my_turtle.setheading(my_turtle.heading() + 10)
#
#
# def rotate_anti():
#     my_turtle.setheading(my_turtle.heading() - 10)
#
#
# def clear():
#     my_turtle.clear()
#     my_turtle.hideturtle()
#     my_turtle.penup()
#     my_turtle.setx(0)
#     my_turtle.sety(0)
#     my_turtle.setheading(0)
#     my_turtle.pendown()
#     my_turtle.showturtle()
#
#
# my_screen.listen()
#
# my_screen.onkey(key="w", fun=move_forward)
# my_screen.onkey(key="s", fun=move_backward)
# my_screen.onkey(key="a", fun=rotate_clock)
# my_screen.onkey(key="d", fun=rotate_anti)
# my_screen.onkey(key="c", fun=clear)

from turtle import Turtle, Screen
from random import randint

colors = ["red", "blue", "yellow", "orange", "green", "purple"]
turtle_array = []
my_screen = Screen()
my_screen.setup(width=500, height=400)


def create_turtles():
    i = 0
    for color in colors:
        turtle_array.append(Turtle(shape="turtle"))
        turtle_array[i].color(color)
        turtle_array[i].penup()
        i += 1


def disperse_turtles():
    xi = -240
    yi = -120
    for turtle in turtle_array:
        turtle.goto(x=xi, y=yi)
        yi = yi + 50


def make_bet():
    return my_screen.textinput(title="Bet Your Turtle", prompt="Name the color of turtle you wanna bet?")


usr_input = make_bet()
create_turtles()
disperse_turtles()
check = True
while check:
    for turtles in turtle_array:
        turtles.forward(randint(0, 10))
        if turtles.xcor() >= 225:
            if turtles.pencolor() == usr_input:
                print(f"You Win!The {usr_input} turtle wins:")
            else:
                print(f"You lose the {turtles.pencolor()} turtle  Wins!")
            check = False
            break
