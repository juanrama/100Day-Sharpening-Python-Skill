from turtle import Turtle
STARTING_POSITION = (0,0)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('purple')
        self.penup()
        self.move_x = 10
        self.move_y = 10
        self.move_speed = 0.1
    
    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)
    
    def reset(self):
        self.goto(0,0)
        self.move_x = 10
        self.move_y = 10
        self.move_speed = 0.1
    
    def bounce_y(self):
        self.move_y *= -1
    
    def bounce_x(self):
        self.move_x *= -1
        self.move_speed *= 0.9
    
    # def move_left(self):
    #     new_x = self.xcor() - 20
    #     self.goto(new_x, 0)
        
    # def move_right(self):
    #     new_x = self.xcor() + 20
    #     self.goto(new_x, 0)
        
        
        
        
    