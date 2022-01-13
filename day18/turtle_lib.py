from turtle import Turtle, Screen
from random import randint, choice
from main import color_list

turtle_screen = Screen()
turtle_screen.colormode(255)

timmy = Turtle()
timmy.shape("turtle")
timmy.color("DarkSeaGreen")
timmy.speed('fastest')
timmy.penup()
timmy.setx(-200)
timmy.sety(-200)
for _ in range(10):
    for _ in range(10):
        timmy.pencolor(choice(color_list))        
        timmy.forward(50)
        timmy.dot(20)
    timmy.left(90)
    timmy.forward(50)
    timmy.left(90)
    timmy.forward(500)
    timmy.left(180)    

turtle_screen.exitonclick()    
        
    
    
    
            
