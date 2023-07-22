from PyQt6.QtWidgets import QPushButton
from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtCore import QUrl, QPropertyAnimation


class Menu_button_creator:

    @staticmethod
    def set_button(sound_file_name, image, button):
        button.animation = QPropertyAnimation(button, b"geometry")
        button.animation.setDuration(2000)




    @staticmethod
    def sound_button_hover(sound_file_name):
        global effect
        effect = QSoundEffect()
        effect.setSource(QUrl.fromLocalFile(sound_file_name))
        effect.setVolume(0.5)
        # possible bug: QSoundEffect::Infinite cannot be used in setLoopCount
        effect.setLoopCount(1)
        effect.play()
