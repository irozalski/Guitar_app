from functools import partial

from PyQt6.QtCore import QPropertyAnimation, QMargins, QAbstractAnimation
from PyQt6.QtWidgets import QPushButton, QGraphicsColorizeEffect
from PyQt6.QtGui import QEnterEvent


class Menu_button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(100)


        # self.colorEffect = QGraphicsColorizeEffect(self)
        # self.colorEffect.setStrength(0)
        # self.colorEffect.setColor(255,0,0)
        # self.colorAnimation = QPropertyAnimation(self.colorEffect, b"strength")
        # self.colorAnimation.setDuration(1000)
        #self.setStyleSheet(""" """)

    def enterEvent(self, event):
        self.animation.setDirection(self.animation.Direction.Forward)
        if self.animation.state() == self.animation.State.Stopped:
            rectangle = self.geometry()
            self.animation.setStartValue(rectangle)
            rectangle += QMargins(5,5,5,5)
            self.animation.setEndValue(rectangle)
            self.animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.animation.setDirection(self.animation.Direction.Backward)
        if self.animation.state() == self.animation.State.Stopped:
            self.animation.start()
        super().leaveEvent(event)




