from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QFont
from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtCore import QUrl

class Sound_button(QPushButton):

    def __init__(self, window, x_cor, y_cor, wg, hg, sound_file_name, image):
        super().__init__(window)
        self.setGeometry(x_cor, y_cor, wg, hg)
        self.setStyleSheet(image)
        self.clicked.connect(lambda: self.sound_button_click(sound_file_name))

    def sound_button_click(self, sound_file_name):
        global effect
        effect = QSoundEffect()
        effect.setSource(QUrl.fromLocalFile(sound_file_name))
        effect.setVolume(0.5)
        # possible bug: QSoundEffect::Infinite cannot be used in setLoopCount
        effect.setLoopCount(1)
        effect.play()
