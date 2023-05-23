import sys
from PyQt6.QtWidgets import QApplication
from window import Window
from Chord import Chord
from Tuner import Tuner
from Metronome import Metronome
from Quiz import Quiz, Question
import akord_base


app = QApplication(sys.argv)

window = Window()

akord_list = []


akord_dict = akord_base.config

for akord in akord_dict:
    akord = Chord(variant=akord_dict[akord]["variant"], x_cor=akord_dict[akord]["x_cor"], y_cor=akord_dict[akord]["y_cor"], wg=akord_dict[akord]["wg"], hg=akord_dict[akord]["hg"],
                  image_7=akord_dict[akord]["image_7"], image_dur=akord_dict[akord]["image_dur"], image_mol=akord_dict[akord]["image_mol"],
                  sound_7=akord_dict[akord]["sound_7"], sound_dur=akord_dict[akord]["sound_dur"], sound_mol=akord_dict[akord]["sound_mol"])
    akord_list.append(akord)

for akord in akord_list:
    akord.create_new_window()
    akord.create_button(window)


tuner = Tuner( x_cor=600, y_cor=100, wg=150, hg=150,
                image_e6="border-image:url(C-7.png)", image_a="border-image:url(C-dur.png)", image_d="border-image:url(C-mol.png)",
                image_g="border-image:url(C-mol.png)", image_b="border-image:url(C-mol.png)", image_e1="border-image:url(C-mol.png)",
                sound_e6="Sounds/E6.wav", sound_a="Sounds/A.wav", sound_d="Sounds/D.wav", sound_g="Sounds/G.wav",
                sound_b="Sounds/B.wav", sound_e1="Sounds/E1.wav")

metronome = Metronome(x_cor=60, y_cor=100, wg=150, hg=150, image_7="border-image:url(C-7.png)", sound_7="Sounds/metron_tick.wav")

question_bank = []

for akord in akord_dict:
    question_sound1 = akord_dict[akord]["sound_7"]
    question_sound2 = akord_dict[akord]["sound_dur"]
    question_sound3 = akord_dict[akord]["sound_mol"]
    question_answer1 = akord_dict[akord]["image_7"]
    question_answer2 = akord_dict[akord]["image_dur"]
    question_answer3 = akord_dict[akord]["image_mol"]
    new_question1 =  Question(question_sound=question_sound1, question_answer=question_answer1)
    new_question2 =  Question(question_sound=question_sound2, question_answer=question_answer2)
    new_question3 =  Question(question_sound=question_sound3, question_answer=question_answer3)

    question_bank.append(new_question1)
    question_bank.append(new_question2)
    question_bank.append(new_question3)

#quiz_brain = QuizBrain(new_question)
print(question_bank[2].question_sound)
print(question_bank[2].question_answer)

quiz = Quiz(variant="Quiz", x_cor=320, y_cor=200, wg=150, hg=50, question_list=question_bank)


tuner.create_button(window)
tuner.create_new_window()
metronome.create_button(window)
quiz.create_button(window)

quiz.next_question()


window.create_logo()



#if __name__ = "__main__":
window.show()

sys.exit(app.exec())
