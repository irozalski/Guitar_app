from functools import partial

from PyQt6.QtWidgets import QPushButton


class Image_button(QPushButton):

    def __init__(self, window, x_cor, y_cor, wg, hg, image, clicked):
        super().__init__(window)
        self.setGeometry(x_cor, y_cor, wg, hg)
        self.setStyleSheet(image)
        self.image = image
        self.clicked.connect(partial(clicked, image))




