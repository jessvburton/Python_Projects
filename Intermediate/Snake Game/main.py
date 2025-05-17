from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.position_up,"Up")
screen.onkey(snake.position_down, "Down")
screen.onkey(snake.position_left, "Left")
screen.onkey(snake.position_right, "Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect collision with wall
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        score.reset()
        snake.reset()

    # Detect collision with tail
    for block in snake.blocks[1:]:
        if snake.snake_head.distance(block) < 10:
            score.reset()
            snake.reset()


screen.exitonclick()
