from turtle import Turtle
from turtle import Screen
import random
COLOR = ['blue', 'yellow', 'green', 'red', 'purple']
CAR = []
scr = Screen()
for i in range(1, 6):
    scr.register_shape(f'car {i}.gif')
    CAR.append(f'car {i}.gif')

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(random.choice(CAR))
        self.shapesize(stretch_len = 2)
        self.color(random.choice(COLOR))
        self.penup()
        self.goto(320, random.randrange(-230, 230, 10))
        self.setheading(180)
        self.speed = 5
    
    def move(self):
        self.fd(self.speed)
        if self.xcor() <= -300:
            self.goto(320, random.randrange(-230, 230, 10))
    
    def add_speed(self):
        self.speed += 2
    
    def reset_car(self):
        self.goto(320, random.randrange(-230, 230, 10))
    
    def reset_speed(self):
        self.speed = 5
        