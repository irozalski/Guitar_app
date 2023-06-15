from PyQt6.QtWidgets import QLabel, QWidget, QVBoxLayout


class Score(QLabel):
    def __init__(self, score, parent = None):
        super().__init__(parent)
        #layout = QVBoxLayout()

        self.setStyleSheet("background-color: yellow; font-size: 20px; padding: 10px;")

        #self.setLayout(layout)
        #self.label = QLabel(str(score),self)
        #layout.addWidget(self.label)

        self.setText(f"Your score: {str(score)}")
        self.setGeometry(270, 20, 250,50)
        self.show()