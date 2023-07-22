from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QFont
from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtCore import QUrl

class Sound_button_creator:

    @staticmethod
    def set_button(sound_file_name, image, button):
        button.setStyleSheet(image)
        try:
            button.clicked.disconnect()
        except TypeError:
            pass
        finally:
            button.clicked.connect(lambda: Sound_button_creator.sound_button_click(sound_file_name))

    @staticmethod
    def sound_button_click(sound_file_name):
        global effect
        effect = QSoundEffect()
        effect.setSource(QUrl.fromLocalFile(sound_file_name))
        effect.setVolume(0.5)
        # possible bug: QSoundEffect::Infinite cannot be used in setLoopCount
        effect.setLoopCount(1)
        effect.play()
