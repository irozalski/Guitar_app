import subprocess

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget
from ChordsWindow import ChordsWindow
from PyQt6.QtGui import QFont
from Menu_button import Menu_button
from Sound_button_creator import Sound_button_creator
#import signal_graph

class Tuner(QWidget):
    def __init__(self, image_e6, image_a, image_d, image_g, image_b, image_e1, sound_e6, sound_a, sound_d, sound_g, sound_b, sound_e1):
        super().__init__()
        #self.new_window = ChordsWindow("Tuner")
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
        uic.loadUi("tuner_window.ui", self)
        self.initUi(sound_e6, sound_a, sound_d, sound_g, sound_b, sound_e1, image_e6, image_a, image_d, image_g, image_b, image_e1)

    def initUi(self, sound_e6, sound_a, sound_d, sound_g, sound_b, sound_e1, image_e6, image_a, image_d, image_g, image_b, image_e1):
        self.graph_button.clicked.connect(lambda: self.run_tuner_graph())
        self.create_sound_button(sound_file_name=sound_e6, image=image_e6, button=self.E6_Button)
        self.create_sound_button(sound_file_name=sound_a, image=image_a, button=self.A_Button)
        self.create_sound_button(sound_file_name=sound_d, image=image_d, button=self.D_Button)
        self.create_sound_button(sound_file_name=sound_g, image=image_g, button=self.G_Button)
        self.create_sound_button(sound_file_name=sound_b, image=image_b, button=self.B_Button)
        self.create_sound_button(sound_file_name=sound_e1, image=image_e1, button=self.E1_Button)

    def create_sound_button(self, sound_file_name, image, button):
        Sound_button_creator.set_button(sound_file_name, image, button)

    def create_new_window(self):
        # self.new_window.create_sound_button(sound_file_name=self.sound_e6, image=self.image_e6)
        # self.new_window.create_sound_button(sound_file_name=self.sound_a, image=self.image_a)
        # self.new_window.create_sound_button(sound_file_name=self.sound_d, image=self.image_d)
        # self.new_window.create_sound_button(sound_file_name=self.sound_g, image=self.image_g)
        # self.new_window.create_sound_button(sound_file_name=self.sound_b, image=self.image_b)
        # self.new_window.create_sound_button(sound_file_name=self.sound_e1, image=self.image_e1)
        pass

    def run_tuner_graph(self):
        print("try")
        script_path = 'signal_graph.py'  # Replace with the actual path
        try:
            subprocess.run(['python', script_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running the script: {e}")

    def on_click(self):
        self.show()
