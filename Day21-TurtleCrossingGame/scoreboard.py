from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color('black')
        self.penup()
        self.setpos(-270, 270)
        self.update()
        self.hideturtle()
        
    
    def update(self):
        self.write(f'Level : {self.level}',font=('Arial', 15, 'normal'))
    
    def add_level(self):
        self.level += 1
        self.clear()
        self.update()
    
    def reset_level(self):
        self.level = 1
        self.clear()
        self.update()
        