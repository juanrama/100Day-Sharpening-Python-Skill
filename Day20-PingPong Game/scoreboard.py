from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_p1 = 0
        self.score_p2 = 0
        self.penup()
        self.color('white')
        self.setpos(0, 270)
        self.update_score()
        self.hideturtle()
    
    def update_score(self):
        self.write(f"P1 : {self.score_p1} | P2 : {self.score_p2}  ", False, "center", font=('Arial', 20, 'normal'))
    
    def add_score_p1(self):
        self.score_p1 += 1
        self.clear()
        self.update_score()
    
    def add_score_p2(self):
        self.score_p2 += 1
        self.clear()
        self.update_score()
    
    # def zero_score(self):
    #     self.score_p1 = 0
    #     self.score_p2 = 0
    #     self.clear()
    #     self.update_score()    