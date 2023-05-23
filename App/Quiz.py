import random
import time

from PyQt6.QtWidgets import  QWidget

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QPushButton
import window as window

class Quiz:

    def __init__(self, variant, x_cor, y_cor, wg, hg, question_list):
        self.variant = variant
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.wg = wg
        self.hg = hg
        self.new_window = window.ChordsWindow(self.variant)
        self.question_list = question_list
        self.question_number = random.randrange(0, 12)
        self.score = 0

    def create_button(self, window):
        button = QPushButton(self.variant, window)
        button.setFont(QFont("Times", 15))
        button.setGeometry(self.x_cor, self.y_cor, self.wg, self.hg)
        button.setStyleSheet("color: rgb(255, 255, 255)")
        button.clicked.connect(self.on_click)


    def on_click(self):
        self.new_window.show()
        self.next_question()



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







class Question:
    def __init__(self, question_sound, question_answer):
        self.question_sound = question_sound
        self.question_answer = question_answer


