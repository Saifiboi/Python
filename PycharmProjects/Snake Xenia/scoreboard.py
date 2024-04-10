from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.write(arg=f"Score:{self.score}", move=False, align="center", font=('Times New Roman', 18, 'normal'))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score:{self.score}", move=False, align="center", font=('Times New Roman', 18, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over!", move=False, align="center", font=('Times New Roman', 18, 'normal'))
