from turtle import Turtle

STARTING_POSITION = (0,-280)
MOVE_ITERATION = 10

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
    
    def move_up(self):
        self.fd(MOVE_ITERATION)
    
    def move_down(self):
        if self.ycor() > -280:
            self.backward(MOVE_ITERATION)
    
    def reset_player(self):
        self.goto(STARTING_POSITION)
        