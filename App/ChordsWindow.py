from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QIcon
from Sound_button import Sound_button
from Image_button import Image_button

class ChordsWindow(QMainWindow):
    def __init__(self, variant):
        super().__init__()
        self.setWindowTitle(variant)
        self.setWindowIcon(QIcon("Images/icon.png"))
        self.setFixedHeight(600)
        self.setFixedWidth(800)
        self.setStyleSheet("background-image:url(Images/new_background2.png); background-attachment: fixed")

    def create_sound_button(self, x_cor, y_cor, wg, hg, sound_file_name, image):
        Sound_button(self, x_cor, y_cor, wg, hg, sound_file_name, image)

    def create_image_button(self, x_cor, y_cor, wg, hg, image, correct_image, clicked):
        Image_button(self, x_cor, y_cor, wg, hg, image, correct_image,clicked)