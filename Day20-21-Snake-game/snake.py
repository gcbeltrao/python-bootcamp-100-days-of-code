from turtle import Turtle

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_AMOUNT = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_squares = []
        self.create_snake()
        self.head = self.snake_squares[0]

    def create_snake(self):
        for point in START_POSITION:
            self.add_segment(point)

    def add_segment(self, point):
        tim = Turtle(shape="square")
        tim.pu()
        tim.color("white")
        tim.goto(point)
        self.snake_squares.append(tim)

    def extend_snake(self):
        self.add_segment(self.snake_squares[-1].position())

    def move(self):
        for snake in range(len(self.snake_squares) - 1, 0, -1):
            new_x = self.snake_squares[snake - 1].xcor()
            new_y = self.snake_squares[snake - 1].ycor()
            self.snake_squares[snake].goto(new_x, new_y)
        self.snake_squares[0].forward(MOVE_AMOUNT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
