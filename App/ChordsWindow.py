from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QIcon
from Sound_button import Sound_button
from Image_button import Image_button
from Score import Score
from Highscore import Highscore

class ChordsWindow(QMainWindow):
    def __init__(self, variant):
        super().__init__()
        self.setWindowTitle(variant)
        self.setWindowIcon(QIcon("Images/icon.png"))
        self.setFixedHeight(600)
        self.setFixedWidth(800)
        #self.setStyleSheet("background-image:url(Images/new_background2.png); background-attachment: fixed")
        self.setStyleSheet("background-color: cyan;")

    def create_sound_button(self, x_cor, y_cor, wg, hg, sound_file_name, image):
        return Sound_button(self, x_cor, y_cor, wg, hg, sound_file_name, image)

    def create_image_button(self, x_cor, y_cor, wg, hg, image, clicked):
        return Image_button(self, x_cor, y_cor, wg, hg, image, clicked)

    def create_score_label(self, score):
        return Score(score=score, parent=self)

    def create_highscore_label(self, highscore):
        return Highscore(highscore=highscore, parent=self)

    def good_answer_screen(self):
        self.setStyleSheet("background-color: green;")
        QTimer.singleShot(600, lambda: self.setStyleSheet("background-color: cyan;"))

    def bad_answer_screen(self):
        self.setStyleSheet("background-color: red;")
        QTimer.singleShot(600, lambda: self.setStyleSheet("background-color: cyan;"))
