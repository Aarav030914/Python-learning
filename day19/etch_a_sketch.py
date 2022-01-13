from turtle import Turtle, Screen

screen = Screen()

timmy = Turtle()
timmy.shape("turtle")

def move_forward():
    timmy.forward(10)
def move_clock():
    timmy.right(3)
def move_anti_clock():
    timmy.left(3)    
def move_back():
    timmy.backward(10)
def clear_screen():
    screen.clearscreen()

screen.listen()  

screen.onkeypress(key = 'w', fun = move_forward)
screen.onkeypress(key = 'd', fun = move_clock)
screen.onkeypress(key = 'a', fun = move_anti_clock)
screen.onkeypress(key = 's', fun = move_back)
screen.onkeypress(key = 'c', fun = clear_screen)

screen.exitonclick()
