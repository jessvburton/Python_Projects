import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move_forward,"Up")

loop_count = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.move()

    # Check for collisions with cars
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            score.game_over()

    # Check if finish line has been reached
    if player.finish_line_check():
        player.reset()
        score.increase_lvl()
        car_manager.incr_speed()

    loop_count += 1
    car_manager.create_car(loop_count)

screen.exitonclick()
