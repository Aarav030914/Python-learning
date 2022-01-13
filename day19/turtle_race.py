from turtle import Turtle, Screen, xcor
from random import randint
screen = Screen()
screen.setup(width = 500, height = 400)
userbet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? green/red/blue/pink. Enter the color:")
colors = ["green", "red", "blue", "pink"]

turtles = []
for i in range(4):
    my_turtle = Turtle(shape = "turtle")
    my_turtle.color(colors[i])    
    my_turtle.penup()
    my_turtle.goto(x = -230, y = -100 + 60*i)
    turtles.append(my_turtle)   
is_race_on = True
while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_turtle = turtle
            if userbet == winner_turtle.color()[1]:
                print(f"You've won. The winner turtle is {winner_turtle.color()[1]}")
            else:
                print(f"You've lost. The winner turtle is {winner_turtle.color()[1]}")    
        turtle.forward(randint(0,10))








screen.exitonclick()