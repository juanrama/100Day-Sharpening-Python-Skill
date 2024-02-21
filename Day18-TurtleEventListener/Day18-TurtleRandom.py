import random
import turtle as t

tim = t.Turtle()
scr = t.Screen()

t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    
    color = (r, g, b)
    
    return color

colour = ['blue', 'red', 'green']
angle = [0, 90, 180, 270]
tim.pensize(20)

for i in range(1,100):
    tim.color(random_color())
    tim.left(random.choice(angle))
    tim.forward(50)

scr.exitonclick