from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

R_PADDLE_POSITION = (350, 0)
L_PADDLE_POSITION = (-350, 0)

screen = Screen()
ball = Ball()
r_paddle = Paddle(R_PADDLE_POSITION)
l_paddle = Paddle(L_PADDLE_POSITION)


# Screen set-up
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "W")
screen.onkey(l_paddle.move_down, "S")

# Game play
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    ball.move()


screen.exitonclick()