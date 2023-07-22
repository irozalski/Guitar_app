import json

from ChordsWindow import ChordsWindow
from Menu_button import Menu_button


class Chord:

    def __init__(self, variant, image_7, image_dur, image_mol, sound_7, sound_dur, sound_mol):
        self.variant = variant
        self.image_7 = image_7
        self.image_dur = image_dur
        self.image_mol = image_mol
        self.sound_7 = sound_7
        self.sound_dur = sound_dur
        self.sound_mol = sound_mol
        self.window = ChordsWindow(self.variant, self.sound_7, self.sound_dur, self.sound_mol, self.image_7, self.image_dur, self.image_mol )


    def connect_button(self, button):
        button.clicked.connect(self.on_click)

    def on_click(self):
        self.window.show()

    def load_from_json(self, filename):
        with open(filename, "r") as f:
            data = json.loads(f.read())
            self.variant = data["variant"]
            self.image_7 = data["image_7"]
            self.image_dur = data["image_dur"]
            self.image_mol = data["image_mol"]
            self.sound_7 = data["sound_7"]
            self.sound_dur = data["sound_dur"]
            self.sound_mol = data["sound_mol"]






