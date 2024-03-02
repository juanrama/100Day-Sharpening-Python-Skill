from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_bank:QuizBrain):
        self.quiz = quiz_bank
        self.window = Tk()
        self.window.config(background=THEME_COLOR, padx=20, pady=20)
        self.window.title('Quizz')
        
        self.score_num = 0
        
        self.score = Label(text=f"Score : {self.score_num}", background=THEME_COLOR, fg="white", font=('Arial', 10))
        self.score.grid(column=1, row=0, pady=20)
        
        self.canvas = Canvas()
        self.canvas.config(width=300, height=250)
        self.text = self.canvas.create_text(150, 125, width=270, text="INI CUMAN COBA", font=('Arial', 20, 'italic'), fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2)
        
        self.t_button = PhotoImage(file="./images/true.png")
        self.f_button = PhotoImage(file="./images/false.png")
        self.true_button = Button(image=self.t_button,  highlightthickness=0, command=self.true_answer)
        self.false_button = Button(image=self.f_button, highlightthickness=0, command=self.false_answer)
        self.true_button.grid(column=0, row=2, pady=20)
        self.false_button.grid(column=1, row=2, pady=20)
        
        self.get_next_question()
        
        self.window.mainloop()
    
    def get_next_question(self):
        question_text = self.quiz.next_question()
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.text, text = question_text)
        
    
    def true_answer(self):
        self.cek_answer("True")
        
    def false_answer(self):
        self.cek_answer("False")
    
    def cek_answer(self, my_answer):
        if self.quiz.check_answer(my_answer):
            self.canvas.config(bg ="green")
            self.score_num += 1
            self.score.config(text=f"Score : {self.score_num}")
        else:
            self.canvas.config(bg ="red")
            
        if self.quiz.still_has_questions():
            self.window.after(1000, self.get_next_question)
        else:
            self.window.after(1000, self.is_done)

    def is_done(self):
        self.true_button.config(state=DISABLED)
        self.false_button.config(state=DISABLED)
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.text, text=f"You've completed the quiz\nYour final score was: {self.quiz.score}/{self.quiz.question_number}")
        
        