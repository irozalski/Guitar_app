import json
import sys
from PyQt6.QtWidgets import QApplication, QVBoxLayout
from window import Window
from Chord import Chord
from Tuner import Tuner
from Metronome import Metronome
from Quiz import Quiz
from question_model import Question_model
from Score import Score

app = QApplication(sys.argv)

window = Window()

chord_list = []
chords_images_sounds = {}

with open("json_chords_base.json", "r") as f:
    jsonObject = json.loads(f.read())
    for key in jsonObject:
        chord = Chord(variant=jsonObject[key]["variant"], x_cor=jsonObject[key]["x_cor"],
                      y_cor=jsonObject[key]["y_cor"], wg=jsonObject[key]["wg"], hg=jsonObject[key]["hg"],
                      image_7=jsonObject[key]["image_7"], image_dur=jsonObject[key]["image_dur"],
                      image_mol=jsonObject[key]["image_mol"],
                      sound_7=jsonObject[key]["sound_7"], sound_dur=jsonObject[key]["sound_dur"],
                      sound_mol=jsonObject[key]["sound_mol"])
        code = chord.variant.split("_")[0]
        chords_images_sounds[code + "_7"] = chord.image_7, chord.sound_7
        chords_images_sounds[code + "_dur"] = chord.image_dur, chord.sound_dur
        chords_images_sounds[code + "_mol"] = chord.image_mol, chord.sound_mol

        chord_list.append(chord)

for chord in chord_list:
    chord.create_new_window()
    chord.create_button(window)

tuner = Tuner(x_cor=600, y_cor=100,wg=150, hg=150,
              image_e6="border-image:url(C-7.png)", image_a="border-image:url(C-dur.png)",
              image_d="border-image:url(C-mol.png)",
              image_g="border-image:url(C-mol.png)", image_b="border-image:url(C-mol.png)",
              image_e1="border-image:url(C-mol.png)",
              sound_e6="Sounds/E6.wav", sound_a="Sounds/A.wav", sound_d="Sounds/D.wav", sound_g="Sounds/G.wav",
              sound_b="Sounds/B.wav", sound_e1="Sounds/E1.wav")

metronome = Metronome(x_cor=60, y_cor=100,wg=150, hg=150)

tuner.create_button(window)
tuner.create_new_window()
metronome.create_button(window)

quiz = Quiz(x_cor=320, y_cor=160, wg=130, hg=130, chords_images_sounds=chords_images_sounds)
quiz.create_button(window)


#label = Highscore(score="woowo")
#label.move(100,200)

#if __name__ = "__main__":
window.show()

sys.exit(app.exec())
