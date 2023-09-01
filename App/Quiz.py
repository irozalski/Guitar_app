import random
from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
from Sound_button_creator import *
from question_model import Question_model
from functools import partial

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
            self.answer_sound("Sounds/correct_answer.wav", "good")
            self.good_answer_screen()

        else:
            self.chances -= 1
            self.update_chances()
            self.answer_sound("Sounds/bad_answer.wav", "bad")
            if self.chances == 0:
                self.game_over_splash_label.display(900)
                self.last_score_label.setText(f"Score: {self.score}")
                self.last_score_label.display(900)
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
        self.good_answer_splash_label.display(time=600)

    def bad_answer_screen(self):
        self.wrong_answer_splash_label.display(time=600)

    def answer_sound(self, sound_file_name, good_or_bad):
        global effect
        effect = QSoundEffect()
        effect.setSource(QUrl.fromLocalFile(sound_file_name))
        if good_or_bad == "good":
            effect.setVolume(0.1)
        else:
            effect.setVolume(0.02)
        # possible bug: QSoundEffect::Infinite cannot be used in setLoopCount
        effect.setLoopCount(1)
        effect.play()