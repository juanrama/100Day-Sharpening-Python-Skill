from turtle import Turtle, Screen

tim = Turtle()
scr = Screen()


for i in range(3,11):
    angle = 360/i
    for j in range(i):
        tim.right(angle)
        tim.forward(100)
    
    
    
scr.exitonclick()
