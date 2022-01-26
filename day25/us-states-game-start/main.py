import turtle
import pandas
import time
FONT = ("Courier", 12, "normal")
score = 0
data = pandas.read_csv("day25/us-states-game-start/50_states.csv")

tim = turtle.Turtle()
tim.color("black")
tim.hideturtle()
tim.penup()

screen = turtle.Screen()
image = "day25/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_list = data["state"].to_list()
guess_is_on = True
correct_guess = []

while guess_is_on:
    time.sleep(0.1)
    answer = (screen.textinput(title=f"{score}/50 states are correct", prompt="What's the name of any state")).title()
    
    if answer in states_list and answer not in correct_guess:
        state = data[data.state == answer]
        tim.goto(int(state.x), int(state.y))
        tim.write(arg=answer, align="center", font=FONT)
        score += 1
        correct_guess.append(answer)
        states_list.remove(answer)   
    else:
        pass

screen.exitonclick()