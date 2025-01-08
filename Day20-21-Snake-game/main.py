from turtle import Screen
from snake import Snake
from time import sleep
from food import Food
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(height=750, width=750)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    sleep(.08)

    snake.move()

    if snake.head.distance(food) < 20:
        food.refresh_position()
        snake.extend_snake()
        score.score_point()
    if snake.head.xcor() > 370 or snake.head.xcor() < -370 or snake.head.ycor() > 370 or snake.head.ycor() < -370:
        score.game_over()
        game_is_on = False
    for segment in snake.snake_squares[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()



screen.exitonclick()
