from PyQt6.QtGui import QIcon
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