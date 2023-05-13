import turtle

TEXTSIZE = 20


class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup
        self.color("white")
        self.penup
        self.goto(-60, 250)
        self.clear()
        self.write(
            f"Score = {self.score}", align="left", font=("Arial", TEXTSIZE, "normal")
        )

    def gain_score(self):
        self.score += 1
        self.clear()
        self.write(
            f"Score = {self.score}", align="left", font=("Arial", TEXTSIZE, "normal")
        )

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", align="center", font=("Arial", TEXTSIZE, "normal"))
