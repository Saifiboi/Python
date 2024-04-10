import turtle

import pandas

my_screen = turtle.Screen()
my_screen.setup(700, 600)
image = "blank_states_img.gif"
my_screen.addshape(image)
my_turtle = turtle.Turtle(image)
new_frame = pandas.read_csv("50_states.csv")
states_list = new_frame["state"].to_list()
new_states_list = []
guessed_states = []
for i in range(0, len(states_list)):
    new_states_list.append(states_list[i].lower())
j = 0
while j != 50:
    state_name = my_screen.textinput(title=f"Guess the state {j}/50.", prompt="Enter the name of Sate.").lower()
    if state_name == "exit":
        break
    if state_name.lower() in new_states_list and not (state_name.lower() in guessed_states):
        guessed_states.append(state_name.lower())
        j += 1
        state_row = new_frame[new_frame["state"] == state_name.title()]
        text_turtle = turtle.Turtle()
        text_turtle.hideturtle()
        text_turtle.penup()
        text_turtle.goto(int(state_row.x), int(state_row.y))
        print(text_turtle.xcor(), text_turtle.ycor())
        text_turtle.write(state_name.title(), align="center")

rem_list = [state for state in states_list if not(state.lower() in guessed_states)]
new_dat = pandas.Series(rem_list)
new_dat.to_csv("rem.csv")
