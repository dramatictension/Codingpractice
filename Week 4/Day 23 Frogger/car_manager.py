import turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(turtle.Turtle):
    def __init__(self):
        self.cars = []
        self.speed = 5

    def make_car(self):
        coinflip = random.randint(0, 4)
        if coinflip == 1:
            new_car = turtle.Turtle()
            new_car.color(random.choice(COLORS))
            new_car.shape("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.goto(350, random.randint(-250, 250))
            new_car.setheading(180)
            self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            car.forward(self.speed)

    def level_up(self):
        self.speed += 10
        print("go")
