import random
import time
from Menu_button import Menu_button
from PyQt6.QtWidgets import  QWidget

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QPushButton
import window as window

class Quiz:

    def __init__(self, x_cor, y_cor, wg, hg, question_list):
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.wg = wg
        self.hg = hg
        self.new_window = window.ChordsWindow("Quiz")
        self.question_list = question_list
        self.question_number = random.randrange(0, 12)
        self.score = 0

    def create_button(self, window):
        Menu_button("Quiz", window, self.x_cor, self.y_cor, self.wg, self.hg, self.on_click)


    def on_click(self):
        self.new_window.show()
        #self.next_question()



    def next_question(self):
        current_question = self.question_list[self.question_number]
        answer1 = self.question_list[self.question_number + random.randrange(1, 5)]
        answer2 = self.question_list[self.question_number + random.randrange(5, 11)]
        print(self.question_list[self.question_number].question_sound)
        print(self.question_list[self.question_number].question_answer)
        #self.new_window.create_sound_button(image=current_question.question_answer, x_cor=60, y_cor=100, wg=285, hg=197, sound= current_question.question_sound)
        #self.new_window.create_quiz_button(image=answer1.question_answer, x_cor=440, y_cor=100, wg=285, hg=197, answer=current_question.question_answer, guess=answer1.question_answer)
        #self.new_window.create_quiz_button(image=answer2.question_answer, x_cor=60, y_cor=350, wg=285, hg=197, answer=current_question.question_answer, guess=answer2.question_answer)
        #self.new_window.create_quiz_button(image=current_question.question_answer, x_cor=440, y_cor=350, wg=285, hg=197, answer=current_question.question_answer, guess=current_question.question_answer)


    def random_question(self):
        random_quest1 = random.choice(self.question_list)
        random_quest2 = random.choice(self.question_list)
        random_quest3 = random.choice(self.question_list)
        random_quest4 = random.choice(self.question_list)





class Question:
    def __init__(self, question_sound, question_answer):
        self.question_sound = question_sound
        self.question_answer = question_answer


