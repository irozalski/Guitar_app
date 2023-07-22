from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QIcon
from Sound_button_creator import Sound_button_creator
from Menu_button import Image_button
from Score import Score
from Highscore import Highscore
from PyQt6.QtWidgets import QWidget
from PyQt6 import uic

class QuizWindow(QWidget):
    def __init__(self, variant):
        super().__init__()
        uic.loadUi("quiz_window.ui", self)
        self.setWindowTitle(variant)
        self.setWindowIcon(QIcon("Images/icon.png"))
        self.initUi()

    def initUi(self):
        pass