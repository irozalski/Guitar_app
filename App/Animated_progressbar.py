from PyQt6 import QtCore
from PyQt6.QtWidgets import QProgressBar
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve


class Animated_progressbar(QProgressBar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.animation = QPropertyAnimation(self, b"value")
        self.animation.setDuration(3200)

    def expand(self):
        if not self.animation.state() == self.animation.State.Stopped:
            self.animation.stop()
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(100.0)
        self.animation.setEasingCurve(QtCore.QEasingCurve.Type.Linear)
        self.animation.start()

