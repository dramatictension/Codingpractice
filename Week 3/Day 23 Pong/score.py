import turtle

TEXTSIZE = 25


class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.leftscore = 0
        self.rightscore = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.penup()
        self.goto(-50, 250)
        self.clear()
        self.write(
            f"{self.leftscore} : {self.rightscore}",
            align="left",
            font=("Arial", TEXTSIZE, "normal"),
        )

    def scoreleft(self):
        self.leftscore += 1
        self.update()

    def scoreright(self):
        self.rightscore += 1
        self.update()

    def update(self):
        self.clear()
        self.write(
            f"{self.leftscore} : {self.rightscore}",
            align="left",
            font=("Arial", TEXTSIZE, "normal"),
        )
