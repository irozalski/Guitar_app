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
        self.setWindowIcon(QIcon("Images/icon.png"))
        self.setFixedHeight(600)
        self.setFixedWidth(800)
        self.setStyleSheet("background-image:url(Images/background.png); background-attachment: fixed")
        self.pixmap_logo = QPixmap("Images/logo.png")
        self.create_logo()

    def create_logo(self):
        logo = QLabel(self)
        logo.setPixmap(self.pixmap_logo)
        logo.resize(250, 130)
        logo.setScaledContents(True)
        logo.move(280, 25)










