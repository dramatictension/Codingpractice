import time
from turtle import Screen
import player
import car_manager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player1 = player.Player()
scoreboard = Scoreboard()
carmanager = car_manager.CarManager()
screen.listen()
screen.onkeypress(player1.move_forward, "Up")
screen.onkeypress(player1.move_backward, "Down")


game_is_on = True
while game_is_on == True:
    time.sleep(0.1)
    screen.update()

    carmanager.make_car()
    carmanager.move_car()

    for car in carmanager.cars:
        if car.distance(player1) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player1.ycor() > 280:
        carmanager.level_up()
        player1.next_level()
        scoreboard.next_level()


screen.exitonclick()
