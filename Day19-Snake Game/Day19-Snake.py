from turtle import Turtle, Screen
import time
import random as r

scr = Screen()
scr.setup(600, 600)
scr.bgcolor('black')
scr.tracer(0)

ular = []
prev_pos = []

x = 0

for i in range(0,3):
    tim = Turtle()
    tim.shape('square')
    tim.color('white')
    tim.penup()
    tim.setpos(x - i * 20, 0)
    ular.append(tim)
    prev_pos.append(tim.pos())

def f():
    if ular[0].heading() != 0.0:
        ular[0].seth(0)

def up():
    if ular[0].heading() != 90.0:
        ular[0].seth(90)

def left():
    if ular[0].heading() != 180.0:
        ular[0].seth(180)

def bottom():
    if ular[0].heading() != 270.0:
        ular[0].seth(270)    

# makan = Turtle()
# makan.shape('square')
# makan.color('white')
# makan.penup()
# makan.setpos(r.randint(1,300), r.randint(1,300))

# posisi_makan = makan.pos()

game_on = True
# belum_makan = True


while game_on:
    # if belum_makan == False:
    #     makan.setpos(r.randint(1,200), r.randint(1,200))
    #     belum_makan = True
    
    scr.onkey(f, "Right")
    scr.onkey(up, "Up")
    scr.onkey(left, "Left")
    scr.onkey(bottom, "Down")
    scr.listen()
    scr.update()
    time.sleep(0.1)
    for j in range(len(ular)):
        prev_pos[j] = ular[j].pos()
        ular[j].fd(20)
        
        if j > 0:
            ular[j].setpos(prev_pos[j - 1])
            
        # if ular[j].pos() == posisi_makan:
        #     belum_makan = False
        
        if ular[j].pos()[0] > 300:
            ular[j].setpos(-300, prev_pos[j][1])
        elif ular[j].pos()[0] < -300:
            ular[j].setpos(300, prev_pos[j][1])
        elif ular[j].pos()[1] > 300:
            ular[j].setpos(prev_pos[j][0],-300)
        elif ular[j].pos()[1] < -300:
            ular[j].setpos(prev_pos[j][0],300)
            
        
        
        
        
scr.exitonclick()

