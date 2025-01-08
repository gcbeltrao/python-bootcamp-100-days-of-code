from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 335)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def score_point(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False, align="center", font=("Calibri Light", 24, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", False, align="center", font=("Calibri Light", 24, "bold"))