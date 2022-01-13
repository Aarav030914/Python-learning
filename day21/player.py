from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.paddle = []
    def create_paddle(self):
        for i in range(3):
            padl_elm = Turtle()
            padl_elm.color("white")
            padl_elm.shape("square")
                