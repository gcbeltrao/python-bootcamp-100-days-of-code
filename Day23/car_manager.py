from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.move_amount = STARTING_MOVE_DISTANCE
        self.all_cars = []
        self.hideturtle()

    def generate_car(self):
        random_number = random.randint(1, 6)
        if random_number == 1:
            new_turtle = Turtle("square")
            new_turtle.penup()
            new_turtle.shapesize(stretch_wid=1, stretch_len=2)
            new_turtle.setheading(180)
            new_turtle.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_turtle.goto(300, random_y)
            self.all_cars.append(new_turtle)

    def cars_move(self):
        for car in self.all_cars:
            car.forward(self.move_amount)

    def increase_movement_cars(self):
        self.move_amount += MOVE_INCREMENT
