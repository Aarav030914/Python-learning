from turtle import Turtle

class Score:
    def __init__(self, score, snake):
        self.score = score
        self.snake = snake
        self.snake.goto(x= 0, y=280)
        self.snake.write(arg = f"SCORE: {self.score}", align = "center")
        
        
    def update_score(self):
        self.score += 1
        self.snake.goto(x= 0, y=280)
        self.snake.clear()
        self.snake.write(arg = f"SCORE: {self.score}", align = "center")
        
    def game_over(self):
        self.snake.goto(0, 0)
        self.snake.write(arg = "GAME OVER", align = "center")

        

        


        