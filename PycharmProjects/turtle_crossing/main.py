import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from time import sleep

screen = Screen()


def game():
    screen.clear()
    screen.setup(width=600, height=600)
    screen.tracer(0)
    my_player = Player()
    my_cars = CarManager()
    my_score = Scoreboard()
    screen.listen()
    screen.onkeypress(fun=my_player.move, key="Up")
    screen.onkeypress(fun=my_player.r_move, key="Right")
    screen.onkeypress(fun=my_player.l_move, key="Left")
    screen.onkeypress(fun=my_player.b_move, key="Down")
    car_collision = False
    game_is_on = True

    def reset_game():
        my_player.goto(0, -280)
        my_cars.inc_speed()

    while game_is_on:
        if my_player.ycor() == 290:
            res = screen.textinput(title="Do you want to continue:", prompt="Enter yes or no:")
            while not isinstance(res, str):
                res = screen.textinput(title="Invalid !!", prompt="Please enter a valid string.Do you want to restart the Game.")
            if res.lower() == "yes":
                reset_game()
                screen.listen()
                my_score.s_update()
            else:
                sleep(2)
                return res
        my_cars.create_car()
        time.sleep(0.1)
        screen.update()
        my_cars.move()
        for i in my_cars.car_array:
            if my_player.distance(i) < 27:
                car_collision = True
                break
        if car_collision:
            my_score.Game_over()
            screen.update()
            sleep(2)
            res = screen.textinput(title="Continue Prompt", prompt="Do you want to restart the Game.")
            print(res)
            while not isinstance(res, str):
                res = screen.textinput(title="Invalid !!", prompt="Please enter a valid string.Do you want to restart the Game.")
            return res


var = "yes"
while var.lower() == "yes":
    var = game()
