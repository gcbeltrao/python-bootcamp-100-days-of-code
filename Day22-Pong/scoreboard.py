from turtle import Turtle

dashed_line_start = (0, -260)
position_score1 = (-150, 200)
position_score2 = (75, 200)


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score_player1 = 0
        self.score_player2 = 0
        self.scores()

    def dashed_line(self):
        self.setheading(90)
        self.width(5)
        self.goto(dashed_line_start)
        for _ in range(int(13)):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)

    def scores(self):
        self.goto(position_score1)
        self.write(f"{self.score_player1}", font=("Square Deal", 50, "bold"))
        self.goto(position_score2)
        self.write(f"{self.score_player2}", font=("Square Deal", 50, "bold"))

    def player1_score(self):
        self.score_player1 += 1
        self.clear()
        self.dashed_line()
        self.scores()

    def player2_score(self):
        self.score_player2 += 1
        self.clear()
        self.dashed_line()
        self.scores()

    def game_over(self, player):
        self.goto(0, 0)
        self.write(player + " win the game", align="center", font=("Times New Roman", 32, "bold"))
