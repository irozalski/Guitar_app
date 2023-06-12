from PyQt6.QtWidgets import QPushButton


class Image_button(QPushButton):

    def __init__(self, window, x_cor, y_cor, wg, hg, image, correct_image,clicked):
        super().__init__(window)
        self.setGeometry(x_cor, y_cor, wg, hg)
        self.setStyleSheet(image)
        self.clicked.connect(lambda: self.image_button_click())
        self.image = image
        self.correct_image = correct_image
        self.clicked.connect(clicked)


    def image_button_click(self):
        if self.image == self.correct_image:
            print("Wow +1")
            return 1
        else:
            print("oj nienie")
            return 1
