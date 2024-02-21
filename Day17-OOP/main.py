from data import question_data
from quiz import QuestionModel
from QuizBrain import QuizzBrain


question_list = []
for question in question_data:
    question_quest = question['text']
    question_answer = question['answer']
    
    question_final = QuestionModel(question_quest, question_answer)
    
    question_list.append(question_final)

quizz_brain = QuizzBrain(question_list)

quizz_brain.next_question()

