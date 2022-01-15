from turtle import Turtle

class Player(Turtle):
    def __init__(self, x_cord):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=3, stretch_wid=1)
        self.penup()
        self.goto(x_cord, 0)
        self.setheading(90)

    def go_up(self):
        self.forward(10)
    def go_down(self):
        self.backward(10)        


                            
                