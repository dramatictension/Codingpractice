import random
import turtle
from turtlefunctions import *
import colorgram


def random_color(turtle):
    color = random.choice(color_list)
    r, g, b = color
    return turtle.color(r, g, b)


sheldon = turtle.Turtle()
sheldon.shape("turtle")
turtle.colormode(255)
sheldon.speed("fastest")


color_list = [
    (56, 108, 149),
    (226, 132, 55),
    (197, 145, 172),
    (234, 201, 101),
    (145, 81, 54),
    (140, 180, 207),
    (233, 225, 195),
    (138, 130, 73),
    (131, 184, 132),
    (141, 100, 130),
    (218, 94, 61),
    (187, 78, 128),
    (50, 156, 196),
    (65, 156, 88),
    (235, 222, 229),
    (64, 140, 104),
    (213, 178, 193),
    (228, 175, 165),
]
sheldon.penup()
sheldon.setposition(-350, -300)
sheldon.pendown()
current_y_coordinate = sheldon.ycor()

for _ in range(10):
    for _ in range(10):
        random_color(sheldon)
        draw_circle_full(sheldon, 20)
        move_forward(sheldon, 70)
    sheldon.setx(-350)
    current_y_coordinate += 50
    sheldon.sety(current_y_coordinate)


screen = turtle.Screen()
screen = turtle.exitonclick()
