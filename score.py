from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_L = 0
        self.score_R = 0
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.color("DarkRed")
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"{self.score_L} Score {self.score_R}", align=ALIGNMENT, font=FONT)

    def increase_L_score(self):
        self.score_L += 1
        self.clear()
        self.update_scoreboard()

    def increase_R_score(self):
        self.clear()
        self.score_R += 1
        self.update_scoreboard()
