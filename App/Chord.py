import json

from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QSlider, QPushButton, QLabel
import winsound
from window import ChordsWindow
from Menu_button import Menu_button

import random

class Chord:

    def __init__(self, variant, x_cor, y_cor, wg, hg, image_7, image_dur, image_mol, sound_7, sound_dur, sound_mol):
        self.variant = variant
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.wg = wg
        self.hg = hg
        self.new_window = ChordsWindow(self.variant)
        self.image_7 = image_7
        self.image_dur = image_dur
        self.image_mol = image_mol
        self.sound_7 = sound_7
        self.sound_dur = sound_dur
        self.sound_mol = sound_mol

    def create_button(self, window):
        Menu_button(self.variant, window, self.x_cor, self.y_cor, self.wg, self.hg, self.on_click)


    def create_new_window(self):
        self.new_window.create_sound_button(x_cor=60, y_cor=100, wg=285, hg=197, sound_file_name=self.sound_7, image=self.image_7)
        self.new_window.create_sound_button(x_cor=440, y_cor=100, wg=285, hg=197, sound_file_name=self.sound_dur, image=self.image_dur)
        self.new_window.create_sound_button(x_cor=250, y_cor=350, wg=285, hg=197, sound_file_name=self.sound_mol, image=self.image_mol)

    def on_click(self):
        self.new_window.show()

    def load_from_json(self, filename):
        with open(filename, "r") as f:
            data = json.loads(f.read())
            self.variant = data["variant"]
            self.x_cor = data["x_cor"]
            self.y_cor = data["y_cor"]
            self.wg = data["wg"]
            self.hg = data["hg"]
            self.image_7 = data["image_7"]
            self.image_dur = data["image_dur"]
            self.image_mol = data["image_mol"]
            self.sound_7 = data["sound_7"]
            self.sound_dur = data["sound_dur"]
            self.sound_mol = data["sound_mol"]

            #f.close()




