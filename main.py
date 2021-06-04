from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

# Draw the net

net = Turtle()
net.pencolor("white")
net.hideturtle()
net.penup()
screen_height = 600
net.goto(0, -screen_height / 2)
dash_line_width = 15  # needs to be an odd number
net.setheading(90)

for i in range(0, screen_height, dash_line_width):
    if i % 2 != 0:
        net.pendown()
    else:
        net.penup()
    net.forward(dash_line_width)

paddle_r = Paddle(x_position=370)
paddle_l = Paddle(x_position=-370)
ball = Ball()
score_r = Scoreboard(x_pos=50)
score_l = Scoreboard(x_pos=-50)
screen.listen()
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")
screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")

game_is_on = True

while game_is_on:
    ball.move()
    screen.update()
    time.sleep(ball.move_speed)

    # Detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_from_wall()
    # Detect collision with paddles
    if (ball.xcor() > 340 and ball.distance(paddle_r) < 50) or (ball.xcor() < -340 and ball.distance(paddle_l) < 50):
        ball.bounce_from_paddle()

    # Detect if right misses the ball
    if ball.xcor() > 360:
        ball.reset_ball()
        score_l.increase_score()
    # Detect if left misses the ball
    if ball.xcor() < -360:
        ball.reset_ball()
        score_r.increase_score()
screen.exitonclick()
