import turtle as t
import random

t.colormode(255)

tim = t.Turtle()
scr = t.Screen()


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    
    color = (r, g, b)
    
    return color

tim.speed('fastest')
def draw_circle(size_gap):  
    for _ in range(360//size_gap):
        tim.color(random_color())
        tim.setheading(tim.heading() + size_gap)
        tim.circle(100)

draw_circle(10)
        


scr.exitonclick()