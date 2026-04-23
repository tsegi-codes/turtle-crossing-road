from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    def create_cars(self):
        chance_car = random.randrange(1, 4)
        if chance_car == 1:
            new_turtle = Turtle("square")
            new_turtle.shapesize(1,2)
            random_y = random.randint(-250,250)
            new_turtle.color(random.choice(COLORS))
            new_turtle.penup()
            new_turtle.goto(300, random_y)
            self.all_cars.append(new_turtle)
            # new_turtle.setheading(180)
    def move_cars(self):
        for car in self.all_cars:
            car.penup()
            car.backward(self.car_speed)
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
