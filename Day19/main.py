from turtle import Turtle, Screen
from turtle_class import CreateTurtle
from random import randint



screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "blue", "green", "brown", "orange"]
position = [0, 50, -50, 100, -100]
turtles = []

user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Choose your color: ")

for turtle_index in range(5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.up()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-230, position[turtle_index])
    turtles.append(new_turtle)


game_on = False
if user_bet:
    game_on = True

while game_on:

    for turtle in turtles:
        if turtle.xcor() >= 230:
            game_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print("You win!")
            else:
                print(f"You lose, the winner is the {turtle.pencolor()} turtle.")


        move_forwards = randint(0, 10)
        turtle.forward(move_forwards)


screen.exitonclick()