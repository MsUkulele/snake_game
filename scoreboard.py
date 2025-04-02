from turtle import Turtle

SCORE = 0
AlIGNMENT = "center"
FONT = ("Courier", 16, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 270)
        self.penup()
        self.color("white")
        self.write(f"Score:{self.score}", align = AlIGNMENT, font = FONT)
        self.hideturtle()

    def new_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score:{self.score}", align = AlIGNMENT, font = FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align = AlIGNMENT, font = FONT)

        #and here
        # try out branch created

