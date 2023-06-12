import random
from Menu_button import Menu_button
from question_model import Question_model
import ChordsWindow as ChordsWindow
from PyQt6.QtGui import QIcon
from functools import partial
class Quiz:

    def __init__(self,x_cor, y_cor, wg, hg, chords_images_sounds):
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.wg = wg
        self.hg = hg
        self.new_window = ChordsWindow.ChordsWindow("Quiz")
        self.chords_images_sounds = chords_images_sounds
        self.score = 0

        self.correct_image = None
        self.button_question = self.new_window.create_sound_button(x_cor=40, y_cor=150, wg=150, hg=100,
                                                                   sound_file_name=None,
                                                                   image=self.correct_image)
        self.button_answer_1 = self.new_window.create_image_button(x_cor=230, y_cor=150, wg=150, hg=100,
                                                                   image=None,
                                                                   clicked=self.clicked)
        self.button_answer_2 = self.new_window.create_image_button(x_cor=420, y_cor=150, wg=150, hg=100,
                                                                   image=None,
                                                                   clicked=self.clicked)
        self.button_answer_3 = self.new_window.create_image_button(x_cor=610, y_cor=150, wg=150, hg=100,
                                                                   image=None,
                                                                   clicked=self.clicked)





    def create_button(self, window):
        return Menu_button("Quiz", window, x_cor=self.x_cor, y_cor=self.y_cor, wg=self.wg, hg=self.hg, on_click=self.on_click)



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
        self.update_image(button=self.button_question, image=self.correct_image,connect=False)
        self.update_image(button=self.button_answer_1, image=self.chords_images_sounds[answer1][0], connect=True)
        self.update_image(button=self.button_answer_2, image=self.chords_images_sounds[answer2][0],connect=True)
        self.update_image(button=self.button_answer_3, image=self.chords_images_sounds[answer3][0],connect=True)

    def on_click(self):
        self.next_question()
        self.new_window.show()


    def clicked(self, image):
        print(image, self.correct_image)
        if image == self.correct_image:
            print("Wow +1")
            self.score += 1
            print(self.score)

        else:
            print("oj nienie")
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




