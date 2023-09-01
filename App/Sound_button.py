from PyQt6.QtCore import QPropertyAnimation, QMargins, QUrl
from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtWidgets import QPushButton, QGraphicsColorizeEffect
from PyQt6.QtGui import QColor


class Sound_button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(100)
        self.colorEffect = QGraphicsColorizeEffect(self)
        self.colorEffect.setStrength(0)
        self.colorEffect.setColor(QColor(0,255,255))
        self.setGraphicsEffect(self.colorEffect)
        self.colorAnimation = QPropertyAnimation(self.colorEffect, b"strength")
        self.colorAnimation.setDuration(300)

    def enterEvent(self, event):
        self.animation.setDirection(self.animation.Direction.Forward)
        self.colorAnimation.setDirection(self.colorAnimation.Direction.Forward)
        if self.animation.state() == self.animation.State.Stopped:
            rectangle = self.geometry()
            self.animation.setStartValue(rectangle)
            rectangle += QMargins(5,5,5,5)
            self.animation.setEndValue(rectangle)
            self.animation.start()

        if self.colorAnimation.state() == self.colorAnimation.State.Stopped:
            self.colorAnimation.setStartValue(0)
            self.colorAnimation.setEndValue(0.7)
            self.colorAnimation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.colorAnimation.setDirection(self.colorAnimation.Direction.Backward)
        self.animation.setDirection(self.animation.Direction.Backward)

        if self.animation.state() == self.animation.State.Stopped:
            self.animation.start()

        if self.colorAnimation.state() == self.colorAnimation.State.Stopped:
            self.colorAnimation.start()
        super().leaveEvent(event)

    def sound_button_click(self, sound_file_name):
        self.colorAnimation.setDuration(600)
        global effect
        effect = QSoundEffect()
        effect.setSource(QUrl.fromLocalFile(sound_file_name))
        effect.setVolume(0.5)
        # possible bug: QSoundEffect::Infinite cannot be used in setLoopCount
        effect.setLoopCount(1)
        effect.play()

    def setup(self, image, sound_file_name, progressbar=None):
        self.setStyleSheet(image)
        self.clicked.connect(lambda: self.sound_button_click(sound_file_name))
        if progressbar is not None:
            self.clicked.connect(lambda: progressbar.expand())

