from PyQt6.QtCore import QTimer, Qt, pyqtSignal
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QMainWindow, QLabel


class Splash_screen(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setWindowIcon(QIcon("Images/icon.png"))
        self.setFixedHeight(700)
        self.setFixedWidth(796)
        #self.setStyleSheet("background-image:url(Images/new_background2.png); background-attachment: fixed")
        self.setStyleSheet("background-color: cyan;")
        self.pixmap_logo = QPixmap("Images/logo.png")
        self.create_splash_logo()
        self.show()
        QTimer.singleShot(1000, lambda: self.closeWindow())

    def create_splash_logo(self):
        logo = QLabel(self)
        logo.setPixmap(self.pixmap_logo)
        logo.resize(375, 130)
        logo.setScaledContents(True)
        logo.move(280, 100)

    def closeWindow(self):
        self.close()

    # def closeEvent(self, event):
    #     self.windowClosed.emit()
    #     event.accept()