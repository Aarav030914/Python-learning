from question_model import Question
from data2 import question_data
from quiz_brain import QuizBrain

question_bank = []
quiz = QuizBrain(question_bank)
for item in question_data:
    question_bank.append(Question(item["question"], item["correct_answer"]))
while quiz.still_has_questions():
    quiz.ask_question()
print(f"Your total score is {quiz.score}")    
    
