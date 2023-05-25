from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title("Classic Snake Game")
scr.tracer(0)

snake = Snake()
food = Food()
score = Score()

scr.listen()

scr.onkey(snake.up, "Up")
scr.onkey(snake.down, "Down")
scr.onkey(snake.left, "Left")
scr.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    scr.update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_segment()
        score.increase_score()

    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        score.game_over()
        game_is_on = False

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.game_over()
            game_is_on = False


scr.exitonclick()
