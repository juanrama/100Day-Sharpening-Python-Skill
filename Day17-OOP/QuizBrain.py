class QuizzBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        
    def next_question(self):
        while self.question_number < len(self.question_list):
            current_question = self.question_list[self.question_number]
            answer = input(f'Q.{self.question_number + 1} : {current_question.question} ? (True/False) ')
            self.question_number += 1
            
            if answer.lower() == current_question.answer.lower():
                print('Jawaban Anda Benar!')
                self.score += 1
            else:
                print('Jawaban Anda Salah')
        
        print('Anda telah menyelesaikan semua soal')
        print(f'Nilai anda adalah : {self.score}')
        
        
        