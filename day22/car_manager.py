from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    
    def __init__(self):
        self.cars = []
           
    def create_cars(self):
        car = Turtle()
        car.penup()
        car.shape("square")
        car.color(COLORS[randint(0,5)])
        car.shapesize(stretch_len=3, stretch_wid=1)
        car.goto(300 + 30*randint(0,5), 15*randint(-16, 17))
        self.cars.append(car)

    def move_cars(self,move_inc):
        move = STARTING_MOVE_DISTANCE + move_inc*MOVE_INCREMENT
        for car in self.cars:
            car.backward(move)    
            
        
