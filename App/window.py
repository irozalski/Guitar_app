from PyQt6.QtWidgets import QPushButton, QLabel, QMainWindow
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtCore import QUrl
import Quiz as Quiz
from Menu_button import Menu_button
from Sound_button import Sound_button
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chords App")
        self.setWindowIcon(QIcon("icon.png"))
        self.setFixedHeight(600)
        self.setFixedWidth(800)
        self.setStyleSheet("background-image:url(background.png); background-attachment: fixed")
        self.pixmap_logo = QPixmap("logo.png")

    def create_logo(self):
        logo = QLabel(self)
        logo.setPixmap(self.pixmap_logo)
        logo.resize(250, 130)
        logo.setScaledContents(True)
        logo.move(280, 25)




class ChordsWindow(QMainWindow):
    def __init__(self, variant):
        super().__init__()
        self.setWindowTitle(variant)
        self.setWindowIcon(QIcon("icon.png"))
        self.setFixedHeight(600)
        self.setFixedWidth(800)
        self.setStyleSheet("background-image:url(new_background2.png); background-attachment: fixed")

    def create_sound_button(self, x_cor, y_cor, wg, hg, sound_file_name, image):
        button = Sound_button(self, x_cor, y_cor, wg, hg, sound_file_name, image)


    def create_quiz_button(self, image, x_cor, y_cor, wg, hg, answer, guess):

        button = QPushButton(self)
        button.setStyleSheet(image)
        button.setGeometry(x_cor, y_cor, wg, hg)
        button.clicked.connect(lambda: quiz_button_click(answer, guess))
        button.clicked.connect(lambda: Quiz.Quiz.next_question(self))


def quiz_button_click(answer, guess):
    if answer == guess:
        print("git")
    else:
        print("nie")


def quiz_btn():
    return True