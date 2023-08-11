from PyQt6 import uic
from PyQt6.QtCore import QTimer, Qt, pyqtSignal
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QMainWindow, QLabel


class Game_over_screen(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setWindowIcon(QIcon("Images/icon.png"))
        self.setFixedHeight(700)
        self.setFixedWidth(796)
        #self.setStyleSheet("background-image:url(Images/new_background2.png); background-attachment: fixed")
        self.setStyleSheet("background-color: yellow;")
        self.pixmap_logo = QPixmap("Images/logo.png")
        self.create_splash_logo()
        self.create_text_label()
        self.show()
        QTimer.singleShot(200, lambda: self.closeWindow())

    def create_splash_logo(self):
        logo = QLabel(self)
        logo.setPixmap(self.pixmap_logo)
        logo.resize(375, 130)
        logo.setScaledContents(True)
        logo.move(280, 100)

    def create_text_label(self):
        text_label = QLabel(self)
        text_label.setText("GAME OVER TRY AGAIN")
        text_label.move(280,400)
        text_label.resize(375, 130)
        #text_label.show()

    def closeWindow(self):
        self.close()
