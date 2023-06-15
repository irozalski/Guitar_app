from PyQt6.QtWidgets import QLabel


class Highscore(QLabel):
    def __init__(self, highscore, parent=None):
        super().__init__(parent)
        # layout = QVBoxLayout()

        self.setStyleSheet("background-color: yellow; font-size: 20px; padding: 10px;")

        # self.setLayout(layout)
        # self.label = QLabel(str(score),self)
        # layout.addWidget(self.label)

        self.setText(f"Highscore: {str(highscore)}")
        self.setGeometry(600, 20, 180, 50)
        self.show()