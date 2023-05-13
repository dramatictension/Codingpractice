import random
import turtle


def change_color(turtle):
    R = random.random()
    B = random.random()
    G = random.random()
    color = (R, G, B)
    return turtle.color(color)


def random_turn(turtle):
    randomdirection = random.choice([90, 180, 270])
    return turtle.right(randomdirection)


def increase_brush_size(turtle):
    new_pensize = turtle.pensize() + 1
    turtle.pensize(new_pensize)
    return turtle.pensize


def increase_turtle_speed(turtle):
    new_speed = turtle.speed() + 1
    turtle.speed(new_speed)
    return turtle.speed


def draw_circle(turtle, circlesize):
    turtle.circle(circlesize)


def draw_circle_full(turtle, circlesize):
    turtle.begin_fill()
    turtle.circle(circlesize)
    turtle.end_fill()


def move_forward(turtle, moveamount):
    turtle.penup()
    turtle.forward(moveamount)
    turtle.pendown


def increase_heading(turtle, increase_amount):
    turtle.setheading(turtle.heading() + increase_amount)
    return turtle.heading


def change_coordinates(turtle, change_x, change_y):
    new_x_cor = turtle.xcor() + change_x
    new_y_cor = turtle.ycor() + change_y
    return turtle.setpos(new_x_cor, new_y_cor)


def set_coordinates(turtle, set_x, set_y):
    if set_x == 0:
        turtle.sety(set_y)
    else:
        turtle.setpos(set_x, set_y)
