from PyQt6.QtWidgets import QWidget
from PyQt6 import uic

class ChordsWindow(QWidget):
    def __init__(self, variant, sound_7, sound_dur, sound_mol, image_7, image_dur, image_mol):
        super().__init__()
        uic.loadUi("chord_window.ui", self)
        self.setWindowTitle(variant)
        self.initUi(sound_7, sound_dur, sound_mol, image_7, image_dur, image_mol)

    def initUi(self, sound_7, sound_dur, sound_mol, image_7, image_dur, image_mol):
        self.Button_7.setup(image_7, sound_7, self.progressBar)
        self.Button_dur.setup(image_dur, sound_dur, self.progressBar)
        self.Button_mol.setup(image_mol, sound_mol, self.progressBar)
        self.progressBar.setValue(0)









