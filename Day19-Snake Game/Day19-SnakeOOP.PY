import turtle as t
from SnakeMoving import Snake
from food import Food
from scoreboard import ScoreBoard
import time

scr = t.Screen()
scr.setup(600, 600)
scr.bgcolor('black')
scr.tracer(0)

snake = Snake()
food = Food()
scbd = ScoreBoard()

game_on = True

while game_on:
    scr.onkey(snake.f, "Right")
    scr.onkey(snake.up, "Up")
    scr.onkey(snake.left, "Left")
    scr.onkey(snake.bottom, "Down")
    scr.listen()
    scr.update()
    time.sleep(0.1)
    snake.move()
    
    if snake.ular[0].distance(food) < 15:
        food.refresh()
        snake.add_snake()
        scbd.add_score()
    
    for i in snake.ular:
        if i == snake.ular[0]:
            pass
        elif snake.ular[0].distance(i) < 10:
            snake.reset_snake()
            scbd.reset()
            


scr.exitonclick()