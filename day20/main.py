from turtle import Screen, Turtle
from snake import Snake
import time
from food import Food
from scoreboard import Score


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Xenia")
screen.tracer(0)

snake_food = Food()

tim = Snake(3, "white", "blue")

score_snake = Turtle()
score_snake.color("white")
score_snake.hideturtle()
score_snake.penup()


score = 0
score_board = Score(score, score_snake)

screen.listen()
screen.onkey(tim.up, "Up")
screen.onkey(tim.down, "Down")
screen.onkey(tim.right, "Right")
screen.onkey(tim.left, "Left")

game_is_on = True
while game_is_on:    
    time.sleep(0.1)
    tim.move()
    screen.update()

    # detect collision with food
    if tim.snake[0].distance(snake_food) < 15:
        snake_food.freshen()
        score_board.update_score()
        tim.extend()
    if tim.head.xcor() > 290 or tim.head.ycor() > 290 or tim.head.xcor() < -290 or tim.head.ycor() < -290:
        game_is_on = False
        score_board.game_over() 
screen.exitonclick()
