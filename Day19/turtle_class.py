from turtle import Turtle, Screen
from random import randint


class CreateTurtle:
    def __init__(self):
        self.turtle = Turtle()

    def move(self):
        number = randint(1, 10)
        self.turtle.forward(number)
