import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_player, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_cars()
    for single_car in car.all_cars:
        if player.distance(single_car) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.is_on_finish_line():
        scoreboard.increase_level()
        player.player_reset()
        car.level_up()


screen.exitonclick()

