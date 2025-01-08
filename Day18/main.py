import turtle as t
from random import choice, randint
import colorgram

turtle = t.Turtle()
turtle.width(5)
turtle.speed("fastest")
t.colormode(255)

image_colors = colorgram.extract("hist_spot_painting.jpg", 30)
# In order to get the colors of a new picture, it is necessary to uncomment the blank color_bank and the first part
# of the hirst_painting function. After the print command, you must copy and paste below to fill the new variable of

# color_bank. color_bank = []
color_bank = [(240, 242, 245), (223, 236, 228), (236, 230, 216), (140, 176, 207), (25, 32, 48), (26, 107, 159), (237, 225, 235), (209, 161, 111), (144, 29, 63), (230, 212, 93), (4, 163, 197), (218, 60, 84), (229, 79, 43), (195, 130, 169), (54, 168, 114), (28, 61, 116), (172, 53, 95), (108, 182, 90), (110, 99, 87), (193, 187, 46), (240, 204, 2), (1, 102, 119), (19, 22, 21), (50, 150, 109), (172, 212, 172), (118, 36, 34), (221, 173, 188), (227, 174, 166), (153, 205, 220), (184, 185, 210)]

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color


def random_direction():
    direction = [0, 90, 180, 270]

    for _ in range(100):
        turtle.color(random_color())
        turtle.forward(25)
        turtle.right(choice(direction))


def draw_shapes():
    n = 3
    while n < 11:
        angle = 360/n
        for _ in range(n):
            turtle.color(random_color())
            turtle.forward(100)
            turtle.right(angle)
        n += 1


def dashed_line():
    for _ in range(10):
        turtle.forward(20)
        turtle.pu()
        turtle.forward(20)
        turtle.pd()


def spirograph(angle):
    turtle.width(0)
    for _ in range(int(360 / angle)):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + angle)


def hirst_painting():
    #This commented code will get the colors of the picture attached with the Colorgram module.
    # for color in image_colors:
    #     r = color.rgb.r
    #     g = color.rgb.g
    #     b = color.rgb.b
    #     new_color = (r, g, b)
    #     color_bank.append(new_color)
    #     print(color_bank)
    turtle.pu()
    turtle.setheading(225)
    turtle.forward(300)
    turtle.setheading(0)
    num_dots = 100

    for dot_count in range(1, num_dots + 1):
        turtle.dot(20, choice(color_bank))
        turtle.forward(50)
        if dot_count % 10 == 0:
            turtle.setheading(90)
            turtle.forward(50)
            turtle.setheading(180)
            turtle.forward(500)
            turtle.setheading(0)


turtle.hideturtle()
hirst_painting()

screen = t.Screen()
screen.exitonclick()
