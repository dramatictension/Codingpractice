import turtle


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_xcor = self.xcor() + self.x_move
        new_ycor = self.ycor() + self.y_move
        self.goto(new_xcor, new_ycor)

    def bounce(self):
        self.y_move *= -1

    # ball bounce behavior when it hits a paddle
    def paddlehit(self):
        self.x_move *= -1

    def recenter(self):
        self.goto(0, 0)
        self.x_move *= -1
