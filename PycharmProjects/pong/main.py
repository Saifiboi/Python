from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from line import Line
from time import sleep


def free_call():
    return True


my_screen = Screen()


def game():
    my_screen.clear()
    my_screen.bgcolor("black")
    my_screen.setup(width=800, height=600)
    my_screen.title(titlestring="Pong")
    my_screen.tracer(0)
    my_paddle = Paddle(370)
    my_paddle2 = Paddle(-380)
    my_screen.update()
    my_screen.tracer(1)
    my_screen.listen()
    my_ball = Ball()
    my_screen.tracer(0)
    player1 = my_screen.textinput(title="Player 1 Name", prompt="Enter the name of player 1")
    while not isinstance(player1, str):
        player1 = my_screen.textinput(title="Invalid Name.", prompt="Please Enter a name!")
    player2 = my_screen.textinput(title="Player 2 Name", prompt="Enter the name of player 2")
    while not isinstance(player2, str):
        player2 = my_screen.textinput(title="Invalid Name.", prompt="Please Enter a name!")
    my_scoreboard = ScoreBoard(player1, player2)
    my_screen.update()
    my_screen.tracer(1)
    my_screen.tracer(0)
    my_line = Line()
    my_screen.update()
    my_screen.tracer(1)
    my_screen.listen()
    my_screen.onkeypress(fun=my_paddle.up_key, key="Up")
    my_screen.onkeypress(fun=my_paddle.down_key, key="Down")
    my_screen.onkeypress(fun=my_paddle2.up_key, key="w")
    my_screen.onkeypress(fun=my_paddle2.down_key, key="s")
    my_screen.onclick(fun=free_call)
    while 1:
        my_ball.move(my_paddle, my_paddle2, my_screen, my_scoreboard)
        if my_scoreboard.l_score == 10:
            my_line.game_over()
            sleep(0.2)
            res = my_screen.textinput(title="Player 1 wins!", prompt="Do you want to continue yes or no:")
            while not isinstance(res, str):
                res = my_screen.textinput(title="Invalid !!",
                                          prompt="Please enter a valid string.Do you want to restart the Game.")
            return res
        elif my_scoreboard.r_score == 10:
            sleep(0.2)
            res = my_screen.textinput(title="Player 1 wins!", prompt="Do you want to continue yes or no:")
            while not isinstance(res, str):
                res = my_screen.textinput(title="Invalid !!", prompt="Please enter a valid string.Do you want to restart the Game.")
            return res


check = "yes"
while check.lower() == "yes":
    check = game()
