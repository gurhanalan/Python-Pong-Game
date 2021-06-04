from turtle import Turtle

FONT = ("Arial", 16, "normal")

class Scoreboard(Turtle):

    def __init__(self, x_pos):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(x_pos, 270)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align="center", font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()