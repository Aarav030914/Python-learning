from turtle import Turtle, color
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self, length, color, h_color):
        self.snake = []
        self.length = length
        self.color = color
        self.h_color = h_color
        self.create_snake()
        self.head = self.snake[0]
        self.head.color(h_color)

    def create_snake(self):

        
        
        for i in range(0, self.length):
            snk_elem = Turtle()
            snk_elem.shape("square")
            snk_elem.color(self.color)
            snk_elem.speed("fastest")
            snk_elem.penup()
            snk_elem.goto(x=0 - i*20, y=0)
            self.snake.append(snk_elem)
    def extend(self):
        snk_elem = Turtle()
        snk_elem.shape("square")
        snk_elem.color(self.color)
        snk_elem.speed("fastest")
        snk_elem.penup()
        snk_elem.goto(self.snake[-1].pos())
        self.snake.append(snk_elem)

    
    
    def move(self):

        for i in range(len(self.snake)-1, 0, -1):
            self.snake[i].goto(self.snake[i-1].pos())
        self.snake[0].forward(20)

    def up(self):
        if self.snake[0].heading() != DOWN:
            self.snake[0].seth(UP)

    def down(self):
        if self.snake[0].heading() != UP:
            self.snake[0].seth(DOWN)

    def right(self):
        if self.snake[0].heading() != LEFT:
            self.snake[0].seth(RIGHT)

    def left(self):
        if self.snake[0].heading() != RIGHT:
            self.snake[0].seth(LEFT)
