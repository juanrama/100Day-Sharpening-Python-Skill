from turtle import Turtle
import random as r

MOVING_DISTANCE = 20

class Snake:
    def __init__(self):
        self.prev_pos = []
        self.ular = []
        self.x = 0
        self.create_snake()
        
    def create_snake(self):
        for i in range(0,3):
            tim = Turtle()
            tim.shape('square')
            tim.color('white')
            tim.penup()
            tim.setpos(self.x - i * 20, 0)
            self.ular.append(tim)
            self.prev_pos.append(tim.pos())
            
    def f(self):
        if self.ular[0].heading() != 0.0 and self.ular[0].heading() != 180.0:
            self.ular[0].seth(0)

    def up(self):
        if self.ular[0].heading() != 90.0 and self.ular[0].heading() != 270.0:
            self.ular[0].seth(90)

    def left(self):
        if self.ular[0].heading() != 180.0 and self.ular[0].heading() != 0.0:
            self.ular[0].seth(180)

    def bottom(self):
        if self.ular[0].heading() != 270.0 and self.ular[0].heading() != 90.0:
            self.ular[0].seth(270)    
    
    def move(self):
        for j in range(len(self.ular)):
            self.prev_pos[j] = self.ular[j].pos()
            self.ular[j].fd(MOVING_DISTANCE)
            
            if j > 0:
                self.ular[j].setpos(self.prev_pos[j - 1])
                
            if self.ular[j].pos()[0] > 300:
                self.ular[j].setpos(-300, self.prev_pos[j][1])
            elif self.ular[j].pos()[0] < -300:
                self.ular[j].setpos(300, self.prev_pos[j][1])
            elif self.ular[j].pos()[1] > 300:
                self.ular[j].setpos(self.prev_pos[j][0],-300)
            elif self.ular[j].pos()[1] < -300:
                self.ular[j].setpos(self.prev_pos[j][0],300)
    
    def add_snake(self):
        tim = Turtle()
        tim.shape('square')
        tim.color('white')
        tim.penup()
        tim.setpos(self.prev_pos[len(self.prev_pos) - 1])
        self.ular.append(tim)
        self.prev_pos.append(tim.pos())
    
    def reset_snake(self):
        for i in self.ular:
            i.goto(1000, 1000)
        self.prev_pos.clear()
        self.ular.clear()
        self.create_snake()
            
        
        
        
    
    

        