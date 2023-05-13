import turtle
import random
from turtle import color as color
from turtlefunctions import *


sheldon = turtle.Turtle()
sheldon.shape("turtle")


for _ in range(1000):
    change_color(sheldon)
    sheldon.forward(50)
    random_turn(sheldon)
    increase_brush_size(sheldon)
    if sheldon.speed() != 10:
        increase_turtle_speed(sheldon)




























screen = turtle.Screen()
screen.exitonclick()