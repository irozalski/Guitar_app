from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QPushButton, QLabel, QMainWindow, QFrame
from PyQt6.QtGui import QIcon, QPixmap


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









