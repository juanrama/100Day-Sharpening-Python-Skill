import turtle as t

tim = t.Turtle()
scr = t.Screen()

def f():
    if tim.heading() != 0.0:
        tim.seth(0)
    tim.fd(50)

def up():
    if tim.heading() != 90.0:
        tim.seth(90)
    else:
        tim.fd(50)

def left():
    if tim.heading() != 180.0:
        tim.seth(180)
    else:
        tim.fd(50)

def bottom():
    if tim.heading() != 270.0:
        tim.seth(270)
    else:
        tim.fd(50)

def clear():
    scr.resetscreen()
    

jalan = True


scr.onkey(f, "Right")
scr.onkey(up, "Up")
scr.onkey(left, "Left")
scr.onkey(bottom, "Down")
scr.onkey(clear, "c")
scr.listen()
scr.exitonclick()
    




