# from turtle import Turtle,Screen
# new_tur = Turtle()
# new_tur.shape("turtle")
# new_tur.color("pink","blue")
#
# new_tur.pencolor("pink")
# new_tur.forward(100)
# new_screen = Screen()
# new_screen.exitonclick()
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon", ["Pikachu", "Squirtle", "charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align="l"
print(table.align)
print(table)
table.align = "c"
print(table.align)
print(table)
