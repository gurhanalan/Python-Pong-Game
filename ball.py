from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        # self.setheading(45)
        self.x_increment = 10
        self.y_increment = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_increment
        new_y = self.ycor() + self.y_increment
        self.goto(new_x, new_y)

    def bounce_from_wall(self):
        self.y_increment *= -1

    def bounce_from_paddle(self):
        self.x_increment *= -1
        self.move_speed *= 0.9

    def reset_ball(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_from_paddle()