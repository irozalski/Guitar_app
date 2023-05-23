from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QFont

class Menu_button(QPushButton):

    def __init__(self, text, window, x_cor, y_cor, wg, hg, on_click):
        super().__init__(text, window)
        self.setGeometry(x_cor, y_cor, wg, hg)
        self.setFont(QFont("Times",15))
        self.setStyleSheet("color: rgb(255, 255, 255)")
        self.clicked.connect(on_click)