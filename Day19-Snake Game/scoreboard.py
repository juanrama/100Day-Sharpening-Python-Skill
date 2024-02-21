from turtle import Turtle

score_list = []
with open('score.txt', mode='r') as s:
    s_read = s.read()
    new_score = map(int, s_read.split()) 
    for i in new_score:
        score_list.append(i)

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = int(score_list[len(score_list) - 1])
        self.penup()
        self.color('white')
        self.setpos(0, 270)
        self.update_score()
        self.hideturtle()
    
    def update_score(self):
        self.write(f"Score : {self.score} | High Score : {self.highscore}", False, "center", font=('Arial', 20, 'normal'))
    
    def add_score(self):
        self.score += 1
        self.clear()
        self.update_score()
    
    def zero_score(self):
        self.score = 0
        self.clear()
        self.update_score()
    
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('score.txt', mode='a') as s:
                s.write(f'\n{self.highscore}')
        self.score = 0
        self.clear()
        self.update_score()