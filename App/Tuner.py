from PyQt6.QtWidgets import QPushButton
from window import ChordsWindow
from PyQt6.QtGui import QFont
from Menu_button import Menu_button


class Tuner:
    def __init__(self, x_cor, y_cor, wg, hg, image_e6, image_a, image_d, image_g, image_b, image_e1, sound_e6, sound_a, sound_d, sound_g, sound_b, sound_e1):
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.wg = wg
        self.hg = hg
        self.new_window = ChordsWindow("Tuner")
        self.image_e6 = image_e6
        self.image_a = image_a
        self.image_d = image_d
        self.image_g = image_g
        self.image_b = image_b
        self.image_e1 = image_e1
        self.sound_e6 = sound_e6
        self.sound_a = sound_a
        self.sound_d = sound_d
        self.sound_g = sound_g
        self.sound_b = sound_b
        self.sound_e1 = sound_e1

    def create_button(self, window):
        Menu_button("Tuner", window, self.x_cor, self.y_cor, self.wg, self.hg, self.on_click)

    def create_new_window(self):
        self.new_window.create_sound_button(x_cor=40, y_cor=150, wg=150, hg=100, sound_file_name=self.sound_e6, image=self.image_e6)
        self.new_window.create_sound_button(x_cor=230, y_cor=150, wg=150, hg=100, sound_file_name=self.sound_a, image=self.image_a)
        self.new_window.create_sound_button(x_cor=420, y_cor=150, wg=150, hg=100, sound_file_name=self.sound_d, image=self.image_d)
        self.new_window.create_sound_button(x_cor=610, y_cor=150, wg=150, hg=100, sound_file_name=self.sound_g, image=self.image_g)
        self.new_window.create_sound_button(x_cor=230, y_cor=350, wg=150, hg=100, sound_file_name=self.sound_b, image=self.image_b)
        self.new_window.create_sound_button(x_cor=420, y_cor=350, wg=150, hg=100, sound_file_name=self.sound_e1, image=self.image_e1)

    def on_click(self):
        self.new_window.show()
