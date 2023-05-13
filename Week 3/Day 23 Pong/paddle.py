import turtle

PADDLESPEED = 20


class Paddle(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
        self.color("white")
        self.speed("fast")

    def go_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + PADDLESPEED
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > -250:
            new_y = self.ycor() - PADDLESPEED
            self.goto(self.xcor(), new_y)

    def stop(self):
        self.direction = 0


class AI_Paddle(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
        self.color("white")
        self.speed("fast")
        self.direction = 1  # start by moving up

    def move(self):
        new_y = self.ycor() + PADDLESPEED * self.direction
        if new_y > 250:
            new_y = 250
            self.direction = -1
        elif new_y < -250:
            new_y = -250
            self.direction = 1
        self.goto(self.xcor(), new_y)
