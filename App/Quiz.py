import random
from Menu_button import Menu_button
from question_model import Question_model
import ChordsWindow as ChordsWindow


class Quiz:

    def __init__(self,x_cor, y_cor, wg, hg, chords_images_sounds):
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.wg = wg
        self.hg = hg
        self.new_window = ChordsWindow.ChordsWindow("Quiz")
        self.chords_images_sounds = chords_images_sounds
        self.score = 0



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
        correctImage, correctSound = self.chords_images_sounds[question.correct]
        button1 = self.new_window.create_sound_button(x_cor=40, y_cor=150, wg=150, hg=100, sound_file_name=correctSound,
                                            image=correctImage)
        self.new_window.create_image_button(x_cor=230, y_cor=150, wg=150, hg=100,
                                            image=self.chords_images_sounds[answer1][0], correct_image=correctImage, clicked=self.clicked)
        self.new_window.create_image_button(x_cor=420, y_cor=150, wg=150, hg=100,
                                            image=self.chords_images_sounds[answer2][0], correct_image=correctImage, clicked=self.clicked)
        self.new_window.create_image_button(x_cor=610, y_cor=150, wg=150, hg=100,
                                            image=self.chords_images_sounds[answer3][0], correct_image=correctImage, clicked=self.clicked)

    def on_click(self):
        self.next_question()
        self.new_window.show()


    def clicked(self):
        self.next_question()






