import json
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QMainWindow
from PyQt6.QtCore import QPropertyAnimation
from window import Window
from Chord import Chord
from Tuner import Tuner
from Metronome import Metronome
from Quiz import Quiz
from Splash_screen import Splash_screen
from question_model import Question_model
from Score import Score


class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main_window.ui", self)
        self.chord_list = []
        self.chords_images_sounds = {}
        self.load_chords()
        self.initUI()


    def load_chords(self):

        with open("json_chords_base.json", "r") as f:
            jsonObject = json.loads(f.read())
            for key in jsonObject:
                chord = Chord(variant=jsonObject[key]["variant"],
                              image_7=jsonObject[key]["image_7"], image_dur=jsonObject[key]["image_dur"],
                              image_mol=jsonObject[key]["image_mol"],
                              sound_7=jsonObject[key]["sound_7"], sound_dur=jsonObject[key]["sound_dur"],
                              sound_mol=jsonObject[key]["sound_mol"])
                code = chord.variant.split("_")[0]
                self.chords_images_sounds[code + "_7"] = chord.image_7, chord.sound_7
                self.chords_images_sounds[code + "_dur"] = chord.image_dur, chord.sound_dur
                self.chords_images_sounds[code + "_mol"] = chord.image_mol, chord.sound_mol

                self.chord_list.append(chord)

    def initUI(self):

        button_list = [self.C_Button, self.D_Button, self.E_Button, self.F_Button, self.G_Button, self.A_Button, self.B_Button,
                       self.Cis_Button, self.Dis_Button, self.Fis_Button, self.Gis_Button, self.H_Button]

        for chord in range(len(self.chord_list)):
            self.chord_list[chord].connect_button(button_list[chord])




        tuner = Tuner(
                      image_e6="border-image:url(C-7.png)", image_a="border-image:url(C-dur.png)",
                      image_d="border-image:url(C-mol.png)",
                      image_g="border-image:url(C-mol.png)", image_b="border-image:url(C-mol.png)",
                      image_e1="border-image:url(C-mol.png)",
                      sound_e6="Sounds/E6.wav", sound_a="Sounds/A.wav", sound_d="Sounds/D.wav", sound_g="Sounds/G.wav",
                      sound_b="Sounds/B.wav", sound_e1="Sounds/E1.wav")

        metronome = Metronome()


        tuner.create_new_window()


        quiz = Quiz(chords_images_sounds=self.chords_images_sounds)


        self.Metronome_Button.clicked.connect(lambda: metronome.on_click())
        self.Quiz_Button.clicked.connect(lambda: quiz.on_click())
        self.Tuner_Button.clicked.connect(lambda: tuner.on_click())
        splash_screen = Splash_screen()






app = QApplication(sys.argv)

window = AppWindow()
#window = Window()





#splash_screen.windowClosed.connect(window.activate)
window.show()

sys.exit(app.exec())
