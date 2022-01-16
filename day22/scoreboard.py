from turtle import Turtle

HORI_LINES = {
    "start_line":[(-300, -250), (300, -250)],
    "end_line":[(-300, 270), (300, 270)]
}
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.play_score = 0
        self.update_score()

    def draw_lines(self, start_pos, end_pos):
        self.penup()
        self.goto(start_pos)
        self.pendown()
        self.goto(end_pos)
        self.penup()
    
    def update_score(self):
        self.clear()
        self.draw_lines(HORI_LINES["start_line"][0],HORI_LINES["start_line"][1])
        self.draw_lines(HORI_LINES["end_line"][0],HORI_LINES["end_line"][1])
        self.goto(-230, 260)
        self.write(arg=f"SCORE:{self.play_score}", align="center", font=FONT)



        
