import random

class Question_model:
    def __init__(self, correct, first_bad_answer, second_bad_answer):
        self.correct = correct
        self.first_bad_answer = first_bad_answer
        self.second_bad_answer = second_bad_answer


    def get_random_answers(self):
        answer_list = [self.correct, self.first_bad_answer, self.second_bad_answer]
        random.shuffle(answer_list)
        return answer_list
