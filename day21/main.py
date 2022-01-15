from turtle import Screen
from player import Player
from score_board import Scoreboard
from pong_ball import Ball
import time 


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)

score = Scoreboard()
score.update_score()


comp_paddle = Player(285)
comp_paddle.goto(285, 40)
play_paddle = Player(-290)

ball = Ball()

screen.listen()
screen.onkey(play_paddle.go_up, "Up")
screen.onkey(play_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    
    if ball.xcor() > 290:
        ball.goto(0, 0)
        ball.move_x *= -1
        score.play_score += 1
        score.update_score()
    
    elif ball.xcor() < -290:
        ball.goto(0, 0)
        ball.move_x *= -1
        score.comp_score += 1
        score.update_score()

    elif ball.xcor() > 278 and ball.distance(comp_paddle) < 50:
        ball.move_x *= -1
    
    elif ball.xcor() < -280 and ball.distance(play_paddle) < 50:
        ball.move_x *= -1


    ball.move()
    screen.update()        
    time.sleep(0.05)



screen.exitonclick()
