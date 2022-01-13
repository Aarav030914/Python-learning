from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.comp_score = 0
        self.play_score = 0
        self.update_score()
    
    def update_score(self):
        self.penup()
        self.clear()
        self.goto(x = -150, y = 250)
        self.pendown()
        self.write(f"{self.comp_score}", align="center", font=("Courier", 10, "normal"))
        self.penup()
        self.goto(x = 150, y = 250)
        self.pendown()
        self.write(f"{self.play_score}", align="center", font=("Courier", 10, "normal"))






