from turtle import Turtle

L_SCOREBOARD_POSITION = (-100, 215)
R_SCOREBOARD_POSITION = (100, 215)
ALIGNMENT = "center"
FONT = ("Arial", 60, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()

        self.goto(L_SCOREBOARD_POSITION)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(R_SCOREBOARD_POSITION)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()
