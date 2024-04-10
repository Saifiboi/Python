from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self,player1,player2):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.l_score=0
        self.r_score=0
        self.l_player_1=player1
        self.r_player_2 = player2
        self.update_score()
    def update_score(self):
        self.clear()
        self.goto(-150, 250)
        self.write(f"{self.l_player_1} {self.l_score}", align="center", font=("Courier", 30, 'normal'))
        self.goto(150, 250)
        self.write(f"{self.r_player_2} {self.r_score}", align="center", font=("Courier", 30, 'normal'))
        # self.goto(0,200)
        # self.pendown()
        # while(self.xcor()>-200):
        #     self.d

    def point_left(self):
        self.l_score+=1
        self.update_score()

    def point_right(self):
        self.r_score += 1
        self.update_score()