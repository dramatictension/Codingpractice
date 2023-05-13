import turtle
import random
from turtle import color as color
from turtlefunctions import *



sheldon = turtle.Turtle()
sheldon.shape("turtle")
sheldon.speed("fastest")

for _ in range(100):
    change_color(sheldon)
    draw_circle(sheldon)
    increase_heading(sheldon, 5)



























screen = turtle.Screen()
screen.exitonclick()