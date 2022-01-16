import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
CAR_DENSITY = 10 # higher the number lower the density

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tim = Player()
score = Scoreboard()

def move():
    tim.forward(10)
screen.listen()
screen.onkey(move, "Up")

traffic = CarManager()

n = 0
game_is_on = True
while game_is_on:
    time.sleep(0.05)
    if n % CAR_DENSITY == 0:
        traffic.create_cars()
    n += 1
    
    for car in traffic.cars:
        if car.xcor() < -320:
            del car
        elif abs(car.ycor() - tim.ycor()) < 12 and car.distance(tim) < 35:
            game_is_on = False

    if tim.ycor() > 270:
        tim.goto(0, -280)
        score.play_score += 1
        score.update_score()           
    
    traffic.move_cars(score.play_score)
    screen.update()    
    

screen.exitonclick()