from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_x = 5
        self.move_y = 5
        

    def move(self):
        if self.ycor() > 170 or self.ycor() < -290:
            self.move_y *= -1

                
        self.goto(self.xcor() + self.move_x, self.ycor() + self.move_y)   

           
            
