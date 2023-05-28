import turtle
import paddle
import ball
import time
import score

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = paddle.Paddle()
l_paddle = paddle.Paddle()
r_paddle.goto(350, 0)
l_paddle.goto(-350, 0)
ball = ball.Ball()
score = score.Score()


screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeyrelease(r_paddle.stop, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeyrelease(r_paddle.stop, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeyrelease(l_paddle.stop, "w")
screen.onkeypress(l_paddle.go_down, "s")
screen.onkeyrelease(r_paddle.stop, "s")

game_is_on = True

while game_is_on == True:
    time.sleep(0.075)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if ball.xcor() > 340 and ball.distance(r_paddle) < 50:
        ball.paddlehit()
    if ball.xcor() < -340 and ball.distance(l_paddle) < 50:
        ball.paddlehit()

    if ball.xcor() > 400:
        score.scoreleft()
        ball.recenter()
    if ball.xcor() < -400:
        score.scoreright()
        ball.recenter()


screen.exitonclick()
