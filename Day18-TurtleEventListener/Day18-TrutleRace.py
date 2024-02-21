import turtle as t
import random as r

scr = t.Screen()
scr.setup(500, 400)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtle = []
jarak = []

x = -230
y = -100

for i in range(len(colors)):
    tim = t.Turtle(shape='turtle')
    tim.color(colors[i])
    tim.penup()
    tim.setpos(x, y)
    y += 40
    turtle.append(tim)
    jarak.append(0)

race_on = True

while race_on == True:
    for i in range(len(turtle)):
        move = r.randint(1,20)
        jarak[i] += move
        turtle[i].fd(move)
        if jarak[i] >= 400:
            print(f'{colors[i]} menang')
            race_on = False
    
    
scr.exitonclick()
    
    