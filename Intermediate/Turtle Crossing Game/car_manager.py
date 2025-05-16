from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self, loop):
        # Create a new car for every 6 loops
        if loop % 6 == 0:
            self.new_car()
        else:
            pass


    def new_car(self):
        new_car = Turtle("square")
        new_car.setheading(180)
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()

        rand_colour = random.choice(COLORS)
        rand_y = random.randint(-250, 250)

        new_car.color(rand_colour)
        new_car.goto(300, rand_y)

        self.cars.append(new_car)


    def move(self):
        for car_num in range(len(self.cars)):
            self.cars[car_num].forward(self.car_speed)

    def incr_speed(self):
        self.car_speed += MOVE_INCREMENT


