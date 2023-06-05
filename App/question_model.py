from window import ChordsWindow
from Menu_button import Menu_button

class Question_model:
    def __init__(self, image, sound):
        self.variant = "Quest"
        self.new_window = ChordsWindow("Quest")
        self.image = image
        self.sound = sound

    def create_button(self, window):
        Menu_button(self.variant, window, x_cor=320, y_cor=200, wg=150, hg=50, on_click=self.on_click)


    def create_new_window(self):
        self.new_window.create_sound_button(x_cor=60, y_cor=100, wg=285, hg=197, sound_file_name=self.sound, image=self.image)
        self.new_window.create_sound_button(x_cor=440, y_cor=100, wg=285, hg=197, sound_file_name=self.sound, image=self.image)
        self.new_window.create_sound_button(x_cor=250, y_cor=350, wg=285, hg=197, sound_file_name=self.sound, image=self.image)

    def on_click(self):
        self.new_window.show()
        # self.next_question()

    def print_self(self):
        print(self.image)
        print(self.sound)

    # def next_question():
    # losowanie nowych
