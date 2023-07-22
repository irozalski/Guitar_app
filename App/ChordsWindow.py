from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QIcon
from Sound_button_creator import Sound_button_creator
from Score import Score
from Highscore import Highscore
from PyQt6.QtWidgets import QWidget
from PyQt6 import uic

class ChordsWindow(QWidget):
    def __init__(self, variant, sound_7, sound_dur, sound_mol, image_7, image_dur, image_mol):
        super().__init__()
        uic.loadUi("chord_window.ui", self)
        self.setWindowTitle(variant)
        #self.setWindowIcon(QIcon("Images/icon.png"))
        #self.setFixedHeight(600)
        #self.setFixedWidth(800)
        #self.setStyleSheet("background-image:url(Images/new_background2.png); background-attachment: fixed")
        #self.setStyleSheet("background-color: cyan;")
        self.initUi(sound_7, sound_dur, sound_mol, image_7, image_dur, image_mol)


    def initUi(self, sound_7, sound_dur, sound_mol, image_7, image_dur, image_mol):
        self.Button_7.setup(image_7, sound_7, self.progressBar)
        self.Button_dur.setup(image_dur, sound_dur, self.progressBar)
        self.Button_mol.setup(image_mol, sound_mol, self.progressBar)
        self.progressBar.setValue(0)









