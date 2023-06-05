import json
import sys
from PyQt6.QtWidgets import QApplication
from window import Window
from Chord import Chord
from Tuner import Tuner
from Metronome import Metronome
from Quiz import Quiz, Question
import akord_base
from question_model import Question_model
import random

app = QApplication(sys.argv)

window = Window()

#akord_list = []

chord_list = []

question_bank = []
#akord_dict = akord_base.config

# for chord in akord_dict:
#    chord = Chord(variant=akord_dict[chord]["variant"], x_cor=akord_dict[chord]["x_cor"], y_cor=akord_dict[chord]["y_cor"], wg=akord_dict[chord]["wg"], hg=akord_dict[chord]["hg"],
#                  image_7=akord_dict[chord]["image_7"], image_dur=akord_dict[chord]["image_dur"], image_mol=akord_dict[chord]["image_mol"],
#                  sound_7=akord_dict[chord]["sound_7"], sound_dur=akord_dict[chord]["sound_dur"], sound_mol=akord_dict[chord]["sound_mol"])
#    akord_list.append(chord)
#
# for chord in akord_list:
#     chord.create_new_window()
#     chord.create_button(window)

with open("json_chords_base.json", "r") as f:
    jsonObject = json.loads(f.read())

    for key in jsonObject:
        chord = Chord(variant=jsonObject[key]["variant"], x_cor=jsonObject[key]["x_cor"], y_cor=jsonObject[key]["y_cor"], wg=jsonObject[key]["wg"], hg=jsonObject[key]["hg"],
                    image_7=jsonObject[key]["image_7"], image_dur=jsonObject[key]["image_dur"], image_mol=jsonObject[key]["image_mol"],
                    sound_7=jsonObject[key]["sound_7"], sound_dur=jsonObject[key]["sound_dur"], sound_mol=jsonObject[key]["sound_mol"])
        chord_list.append(chord)


with open("questions.json", "r") as f:
    jsonObject = json.loads(f.read())

    for question in jsonObject:
        questions = Question_model(image=jsonObject[question])


    f.close()

for chord in chord_list:
    chord.create_new_window()
    chord.create_button(window)


tuner = Tuner( x_cor=600, y_cor=100, wg=150, hg=150,
                image_e6="border-image:url(C-7.png)", image_a="border-image:url(C-dur.png)", image_d="border-image:url(C-mol.png)",
                image_g="border-image:url(C-mol.png)", image_b="border-image:url(C-mol.png)", image_e1="border-image:url(C-mol.png)",
                sound_e6="Sounds/E6.wav", sound_a="Sounds/A.wav", sound_d="Sounds/D.wav", sound_g="Sounds/G.wav",
                sound_b="Sounds/B.wav", sound_e1="Sounds/E1.wav")

metronome = Metronome(x_cor=60, y_cor=100, wg=150, hg=150)



# for x in chord_list:
#     question_sound1 = chord_list[x]["sound_7"]
#     question_sound2 = chord_list[x]["sound_dur"]
#     question_sound3 = chord_list[x]["sound_mol"]
#     question_image1 = chord_list[x]["image_7"]
#     question_image2 = chord_list[x]["image_dur"]
#     question_image3 = chord_list[x]["image_mol"]
#     new_question1 =  Question_model(sound=question_sound1, image=question_image1)
#     new_question2 =  Question_model(sound=question_sound2, image=question_image2)
#     new_question3 =  Question_model(sound=question_sound3, image=question_image3)
#
#     question_bank.append(new_question1)
#     question_bank.append(new_question2)
#     question_bank.append(new_question3)





#question_bank[number].create_button(window)
#question_bank[number].create_new_window()
# #quiz_brain = QuizBrain(new_question)
# print(question_bank[2].question_sound)
# print(question_bank[2].question_answer)
#
# quiz = Quiz(x_cor=320, y_cor=200, wg=150, hg=50, question_list=chord_list)


tuner.create_button(window)
tuner.create_new_window()
metronome.create_button(window)

# quiz.create_button(window)
# quiz.random_question()
#quiz.next_question()

#new_question1.create_button(window)
#new_question1.create_new_window()
window.create_logo()



#if __name__ = "__main__":
window.show()

sys.exit(app.exec())
