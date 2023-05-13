import turtle
import time
from snake import *
from food import *
from score import *

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("NiccSnake!")
screen.tracer(0)

snek = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(snek.go_up, "Up")
screen.onkey(snek.go_down, "Down")
screen.onkey(snek.go_left, "Left")
screen.onkey(snek.go_right, "Right")

ongoing = True
while ongoing:
    screen.update()
    time.sleep(0.07)
    snek.move()
    if snek.head.distance(food) < 15:
        score.gain_score()
        food.reroll()
        snek.extend()
    if (
        snek.head.xcor() > 300
        or snek.head.xcor() < -300
        or snek.head.ycor() > 300
        or snek.head.ycor() < -300
    ):
        ongoing = False
        score.game_over()

    for segment in snek.snake_body[1:]:
        if snek.head.distance(segment) < 10:
            ongoing = False
            score.game_over()

screen.exitonclick()
