from turtle import Turtle

SCOREBOARD_POSITION = (0, 280)
SCORE = 0
ALIGNMENT = "center"
FONT = ("Arial", 10, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = SCORE
        self.hideturtle()
        self.penup()
        self.goto(SCOREBOARD_POSITION)
        self.color("white")
        self.write(f"Score = {SCORE}", align=ALIGNMENT, font=('Arial', 10, 'normal'))

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)



