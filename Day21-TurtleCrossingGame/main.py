from turtle import Screen
from player import Player
from car import Car
from scoreboard import Scoreboard
import time
import random

scr = Screen()
scr.setup(600, 600)
scr.tracer(0)

player = Player()
lvl = Scoreboard()

list_car = []
for i in range(20):
    car = Car()
    list_car.append(car)

game_on = True


scr.onkey(player.move_up, 'Up')
scr.onkey(player.move_down, 'Down')
scr.listen()


while game_on:
    time.sleep(0.1)
    for i in range(len(list_car)):
        if i == 0:
            list_car[i].move() 
        elif list_car[i-1].xcor() < 250 and list_car[i].xcor() == 320:
            list_car[i].move()
        elif list_car[i].xcor() < 320:
            list_car[i].move()

        if player.distance(list_car[i]) < 25:
            player.reset_player()
            for j in range(len(list_car)):
                list_car[j].reset_car()
                list_car[j].reset_speed()
            lvl.reset_level()
    
    if player.ycor() > 280:
        player.reset_player()
        for i in list_car:
            i.reset_car()
            i.add_speed()
        lvl.add_level()
        
    scr.update()
    
scr.exitonclick()