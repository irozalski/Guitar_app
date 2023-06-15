import random
from Menu_button import Menu_button
from question_model import Question_model
import ChordsWindow as ChordsWindow
from PyQt6.QtGui import QIcon
from functools import partial
from Score import Score
import json
class Quiz:

    def __init__(self,x_cor, y_cor, wg, hg, chords_images_sounds):
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.wg = wg
        self.hg = hg
        self.new_window = ChordsWindow.ChordsWindow("Quiz")
        self.chords_images_sounds = chords_images_sounds
        self.score = 0
        self.highscore = self.get_highscore()
        self.question_image = "border-image:url(Images/questionmark.png)"



        self.correct_image = None
        self.button_question = self.new_window.create_sound_button(x_cor=300, y_cor=120, wg=216, hg=144,
                                                                   sound_file_name=None,
                                                                   image=self.question_image)
        self.button_answer_1 = self.new_window.create_image_button(x_cor=70, y_cor=350, wg=216, hg=144,
                                                                   image=None,
                                                                   clicked=self.clicked)
        self.button_answer_2 = self.new_window.create_image_button(x_cor=300, y_cor=350, wg=216, hg=144,
                                                                   image=None,
                                                                   clicked=self.clicked)
        self.button_answer_3 = self.new_window.create_image_button(x_cor=530, y_cor=350, wg=216, hg=144,
                                                                   image=None,
                                                                   clicked=self.clicked)





    def create_button(self, window):
        return Menu_button("Quiz", window, x_cor=self.x_cor, y_cor=self.y_cor, wg=self.wg, hg=self.hg, on_click=self.on_click)

    def create_score_label(self):
        return self.new_window.create_score_label(self.score)

    def create_highscore_label(self):
        return self.new_window.create_highscore_label(self.highscore)

    def good_answer_screen(self):
        return self.new_window.good_answer_screen()

    def bad_answer_screen(self):
        return self.new_window.bad_answer_screen()



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
        self.update_sound(button=self.button_question, sound=correctSound)
        self.update_image(button=self.button_question, image=self.question_image,connect=False)
        self.update_image(button=self.button_answer_1, image=self.chords_images_sounds[answer1][0], connect=True)
        self.update_image(button=self.button_answer_2, image=self.chords_images_sounds[answer2][0],connect=True)
        self.update_image(button=self.button_answer_3, image=self.chords_images_sounds[answer3][0],connect=True)

    def on_click(self):
        self.score = 0
        self.create_score_label()
        self.create_highscore_label()
        self.next_question()
        self.new_window.show()


    def clicked(self, image):
        print(image, self.correct_image)
        if image == self.correct_image:
            self.update_score()
            self.update_highscore()
            self.good_answer_screen()

        else:
            self.bad_answer_screen()
        self.next_question()

    def update_image(self,button, image, connect):
        button.image = image
        button.setStyleSheet(image)
        if connect:
            button.clicked.disconnect()
            button.clicked.connect(partial(self.clicked, image))
        button.update()



    def update_sound(self,button, sound):
        button.sound_file_name = sound
        button.clicked.disconnect()
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
        self.create_score_label()

    def update_highscore(self):
        self.highscore = self.get_highscore()
        self.create_highscore_label()
