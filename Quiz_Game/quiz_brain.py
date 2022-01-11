class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.user_score = 0
        self.question_list = q_list
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        actual_question = self.question_list[self.question_number].text
        actual_answer = self.question_list[self.question_number].answer
        # print(actual_question)
        self.question_number += 1

        user_answer = input(f"Q.{self.question_number}: {actual_question} (True or False)?: ")
        # print(self.question_number)
        if(user_answer.lower() == actual_answer.lower()):
            print("Correct!")
            self.user_score += 1
        else:
            print("Wrong :(")

        print(f"Your score is {self.user_score}/{self.question_number}")