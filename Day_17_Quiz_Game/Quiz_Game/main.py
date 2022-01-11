from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    # print(question)
    new_question = Question(question["text"], question["answer"])
    question_bank.append(new_question)

my_quiz = QuizBrain(question_bank)
while my_quiz.still_has_questions():
    my_quiz.next_question()

print(f"You've completed the Quiz. Your final score is {my_quiz.user_score}/{my_quiz.question_number}")