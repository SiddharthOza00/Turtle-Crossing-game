import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
screen = Screen()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.setup(width=600, height=600)
screen.tracer(0)
game_is_on = True

screen.listen()
screen.onkey(player.go_up, "Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()
    for cars in car_manager.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.at_finishline():
        player.goto_start()
        car_manager.level_up()
        scoreboard.increase_level()
        scoreboard.update_scoreboard()


screen.exitonclick()