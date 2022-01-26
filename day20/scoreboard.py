import os
os.chdir('/home/aarav/Desktop/Python-learning/day20')

from turtle import Turtle

class Score:
    def __init__(self, snake):
        self.score = 0
        
        with open("high_score.txt") as file:
            contents = file.read()
        self.high_score = int(contents)
        
        self.snake = snake
        self.snake.goto(x= 0, y=280)
        self.snake.write(arg = f"SCORE: {self.score} High Score:{self.high_score}", align = "center")
        
        
    def update_score(self):
        self.snake.goto(x= 0, y=280)
        self.snake.clear()
        self.snake.write(arg = f"SCORE: {self.score} High Score:{self.high_score}", align = "center")
        
    def game_over(self):
        self.snake.goto(0, 0)
        self.snake.write(arg = "GAME OVER", align = "center")

        

        


        