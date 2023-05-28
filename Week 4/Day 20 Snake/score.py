import turtle

TEXTSIZE = 20
FONT = ("Courier", 18, "normal")

try:
    with open("Week 3/Day 20 Snake/hiscore.txt", mode="r") as hiscore_file:
        hiscore = hiscore_file.read()
except FileNotFoundError:
    hiscore = "0"
except IOError:
    hiscore = "0"


class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hiscore = hiscore
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-150, 230)
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.hiscore}",
            align="left",
            font=(FONT),
        )

    def reset(self):
        if self.score > int(self.hiscore):
            self.hiscore = self.score
            self.update_scoreboard()
            self.save_newhiscore()
        self.score = 0

    #        self.write("Game Over.", align="center", font=(FONT))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.hiscore}", font=FONT)

    def save_newhiscore(self):
        with open("Week 3\Day 20 Snake\hiscore.txt", mode="w") as hiscoredata:
            hiscoredata.write(str(self.hiscore))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
