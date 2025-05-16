from turtle import Turtle

SCOREBOARD_POSITION = (-290, 270)
SCORE = 0
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = SCORE
        self.hideturtle()
        self.penup()
        self.goto(SCOREBOARD_POSITION)
        self.color("black")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level = {self.score}", align="left", font=FONT)

    def increase_lvl(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=FONT)
