import turtle

sheldon = turtle.Turtle()
screen = turtle.Screen()
sheldon.shape("turtle")
sheldon.color("royalblue")


def move_forwards():
    sheldon.forward(10)


def move_backwards():
    sheldon.backward(10)


def turn_left():
    sheldon.left(5)


def turn_right():
    sheldon.right(5)


def reset():
    sheldon.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=reset)
screen.exitonclick()
