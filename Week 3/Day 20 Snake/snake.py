import turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self) -> None:
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)
        self.snake_body[0].fd(MOVE_DISTANCE)

    def add_segment(self, position):
        new_snake = turtle.Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.snake_body.append(new_snake)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def go_up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)

    def go_down(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)

    def go_left(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)

    def go_right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)
