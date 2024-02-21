import colorgram
import turtle as t
import random as r

tim = t.Turtle()
scr = t.Screen()

t.colormode(255)

colors = colorgram.extract('hirst.jpg', 30)


#Color Palette
list_color = []

def color_split(x):
    r = x.rgb[0]
    g = x.rgb[1]
    b = x.rgb[2]
    
    color = (r, g, b)
    
    return color
    

for i in colors:    
    list_color.append(color_split(i))
    

# Turtle Screen
tim.pensize(20)

upper = [11, 21, 31, 41, 51, 61, 71, 81, 91]
tim.speed('fastest')
tim_y = -80
tim_x = -50
tim.penup()
tim.hideturtle()
tim.setx(tim_x)
tim.sety(tim_y)

for i in range(1, 101):
    if i in upper:
        tim_y += 50
        tim.setx(tim_x)
        tim.sety(tim_y)
    tim.pendown()
    tim.dot(20, r.choice(list_color))
    tim.penup()
    tim.forward(50)



scr.exitonclick()
