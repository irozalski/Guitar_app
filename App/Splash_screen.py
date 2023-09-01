from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QLabel


class Splash_screen(QLabel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setVisible(False)
        self.setStyleSheet("background-color: cyan;")

    def create_splash_logo(self):
        logo = QLabel(self)
        logo.resize(375, 130)
        logo.setScaledContents(True)
        logo.move(280, 100)

    def display(self, time):
        self.setVisible(True)
        QTimer.singleShot(time, lambda: self.setVisible(False))
