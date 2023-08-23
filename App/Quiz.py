import random

from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
from Game_over_screen import Game_over_screen
from Sound_button_creator import *
from Menu_button import Menu_button
from question_model import Question_model
import ChordsWindow as ChordsWindow
from PyQt6.QtGui import QIcon
from functools import partial
from Score import Score
import json
class Quiz(QWidget):

    def __init__(self, chords_images_sounds):
        super().__init__()
        uic.loadUi("quiz_window.ui", self)
        self.chords_images_sounds = chords_images_sounds
        self.correct_image = None
        self.score = 0
        self.chances = 3
        self.highscore = self.get_highscore()
        self.question_image = "border-image:url(Images/icon.png)"
        self.initUi()
        self.next_question()


    def initUi(self):
        self.Highscore_Label.setText(f"Highscore: {self.highscore}")






    def next_question(self):
        all_keys = list(self.chords_images_sounds.keys())
        correct = random.choice(all_keys)
        all_keys.remove(correct)
        bad_answer1 = random.choice(all_keys)
        all_keys.remove(bad_answer1)
        bad_answer2 = random.choice(all_keys)
        question = Question_model(correct=correct, first_bad_answer=bad_answer1, second_bad_answer=bad_answer2)
        answer1, answer2, answer3 = question.get_random_answers()
        self.correct_image, correctSound = self.chords_images_sounds[question.correct]
        #Sound_button_creator.set_button(button=self.Question_Button, sound_file_name=correctSound, image=self.question_image)
        self.Question_Button.setup(self.question_image, correctSound)
        self.update_image(button=self.Answer1_Button, image=self.chords_images_sounds[answer1][0])
        self.update_image(button=self.Answer2_Button, image=self.chords_images_sounds[answer2][0])
        self.update_image(button=self.Answer3_Button, image=self.chords_images_sounds[answer3][0])

    def on_click(self):
        self.score = 0
        self.Score_Label.setText(f"Score: {self.score}")
        self.chances = 3
        self.chance3.show()
        self.chance2.show()
        self.chance1.show()
        self.next_question()
        self.show()


    def clicked(self, image):
        if image == self.correct_image:
            self.update_score()
            self.update_highscore()
            self.good_answer_screen()

        else:
            self.chances -= 1
            self.update_chances()
            if self.chances == 0:
                self.splash_label.display("yellow", "koniec")
                self.on_click()
            else:
                self.bad_answer_screen()
        self.next_question()

    def update_image(self,button, image):
        button.setStyleSheet(image)


        try:
            button.clicked.disconnect()
        except TypeError:
            pass
        finally:
            button.clicked.connect(partial(self.clicked, image))





    def update_sound(self,button, sound):

        button.sound_file_name = sound
        try:
            button.clicked.disconnect()
        except TypeError:
            pass
        finally:
            button.clicked.connect(lambda: button.sound_button_click(sound))


    def get_highscore(self):
        with open("json_highscore.json", "r+") as f:
            jsonObject = json.load(f)
            if self.score > jsonObject["highscore"]:
                jsonObject["highscore"] = self.score
                f.seek(0)  # Move the file cursor to the beginning
                json.dump(jsonObject, f)  # Write the updated high score back to the JSON file
                f.truncate()  # Truncate the remaining content if necessary
            return jsonObject["highscore"]


    def update_score(self):
        self.score += 1
        self.Score_Label.setText(f"Score: {self.score}")

    def update_highscore(self):
        self.highscore = self.get_highscore()
        self.Highscore_Label.setText(f"Highscore: {self.highscore}")

    def update_chances(self):
        if self.chances == 2:
            self.chance3.hide()
        if self.chances == 1:
            self.chance2.hide()
        if self.chances == 0:
            self.chance1.hide()



    def good_answer_screen(self):
        #Game_over_screen()
        #self.setStyleSheet("QWidget{background-color: green;} QPushButton{color: rgb(255, 255, 255);height: 150px;width: 200px; border:3px solid rgb(0,0,0); border-radius:8px;}")
        #QTimer.singleShot(600, lambda: self.setStyleSheet("QWidget{background-color: cyan;} QPushButton{color: rgb(255, 255, 255);height: 150px;width: 200px; border:3px solid rgb(0,0,0); border-radius:8px;}"))
        self.splash_label.display("green", "git")
    def bad_answer_screen(self):
        #Game_over_screen()
        #self.setStyleSheet("QWidget{background-color: red;} QPushButton{color: rgb(255, 255, 255);height: 150px;width: 200px; border:3px solid rgb(0,0,0); border-radius:8px;} ")
        #QTimer.singleShot(600, lambda: self.setStyleSheet("QWidget{background-color: cyan;} QPushButton{color: rgb(255, 255, 255);height: 150px;width: 200px; border:3px solid rgb(0,0,0); border-radius:8px;}"))
        self.splash_label.display("red", "zle")