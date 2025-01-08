from turtle import Screen
from scoreboard import ScoreBoard
from paddle import Paddle
from ball import Ball
from time import sleep

game_is_on = True

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

score = ScoreBoard()
score.dashed_line()

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

ball = Ball()

screen.listen()

screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

while game_is_on:
    sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.kick()
    if ball.xcor() > 390:
        ball.reset_position()
        score.player1_score()
    elif ball.xcor() < -390:
        ball.reset_position()
        score.player2_score()
    if score.score_player1 == 5:
        game_is_on = False
        score.game_over("Player1")
    elif score.score_player2 == 5:
        game_is_on = False
        score.game_over("Player2")

screen.exitonclick()
