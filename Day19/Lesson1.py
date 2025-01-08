from turtle import Turtle, Screen

tom = Turtle()
tim = Turtle()
screen = Screen()


def move_forwards():
    tom.forward(10)


def move_backwards():
    tom.backward(10)


def turn_right():
    tom.right(10)


def turn_left():
    tom.left(10)


def clear():
    # tom.reset()
    tom.clear()
    tom.pu()
    tom.home()
    tom.pd()


# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="a", fun=turn_right)
# screen.onkey(key="d", fun=turn_left)
screen.onkey(key="c", fun=clear)

screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=turn_right)
screen.onkeypress(key="d", fun=turn_left)

screen.listen()
screen.exitonclick()
