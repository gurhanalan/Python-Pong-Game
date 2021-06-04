from turtle import Turtle

UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self, x_position):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x_position, 0)

    # def __init__(self):
    #     self.num_of_segments = 5
    #     self.segments = []
    #     for i in range(self.num_of_segments):
    #         new_turtle = Turtle(shape="square")
    #         new_turtle.penup()
    #         new_turtle.color("white")
    #         new_turtle.goto(-380, -20 * i)
    #         self.segments.append(new_turtle)
    #     self.head = self.segments[0]
    #
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        # self.setheading(UP)
        # self.forward(20)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        # self.setheading(DOWN)
        # self.forward(20)
    #     for i in self.segments:
    #         i.setheading(UP)
    #         i.forward(20)
    #
    # def down(self):
    #     for i in self.segments:
    #         i.setheading(DOWN)
    #         i.forward(20)
