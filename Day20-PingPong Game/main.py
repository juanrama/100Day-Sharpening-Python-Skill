import turtle as t
from pong import Pong
from ball import Ball
from scoreboard import Scoreboard
import time

scr = t.Screen()
scr.setup(800, 600)
scr.bgcolor('black')
scr.tracer(0)

pong_p1 = Pong((350,0))
pong_p2 = Pong((-350,0))
ball = Ball()
game_on = True
score = Scoreboard()

scr.listen()
scr.onkey(pong_p1.up, "Up")
scr.onkey(pong_p1.down, "Down")
scr.onkey(pong_p2.up, "w")
scr.onkey(pong_p2.down, "s")

while game_on == True:
    time.sleep(ball.move_speed)
    scr.update()
    ball.move()
    
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()
        
    if ball.distance(pong_p1) < 50 and ball.xcor() > 320 or ball.distance(pong_p2) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
    if ball.xcor() > 400:
        ball.reset()
        ball.bounce_x()
        score.add_score_p1()
    
    if ball.xcor() < -400:
        ball.reset()
        ball.bounce_x()
        score.add_score_p2()

scr.exitonclick()