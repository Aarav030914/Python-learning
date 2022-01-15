from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):

        super().__init__()
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.comp_score = 0
        self.play_score = 0
        self.update_score()
        
    
    def draw_line(self):
        
        self.goto(-300, 180)
        self.pendown()
        self.forward(600)
        self.penup()    

    
    def update_score(self):
                
        self.goto(x = -150, y = 200)
        self.clear()
        self.write(f"{self.play_score}", align="center", font=("Courier", 50, "normal"))
        self.goto(x = 150, y = 200)
        self.write(f"{self.comp_score}", align="center", font=("Courier", 50, "normal"))
        self.draw_line()






