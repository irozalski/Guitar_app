from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QSlider, QPushButton, QLabel
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QFont, QIcon
import winsound
from Menu_button import Menu_button


class Metronome(QWidget):
    def __init__(self):
        super().__init__()
        self.tempo = 120
        self.is_running = False
        self.setWindowIcon(QIcon("Images/metro_icon2.png"))
        # timer i ustawienie sygnału timeout na funkcje tick()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.tick)

        # widgets
        self.tempo_slider = QSlider()  # Qt.Horizontal
        self.tempo_slider.setMinimum(40)
        self.tempo_slider.setMaximum(220)
        self.tempo_slider.setValue(self.tempo)
        self.tempo_slider.valueChanged.connect(self.set_tempo)

        self.start_stop_button = QPushButton("Start")
        self.start_stop_button.setFixedWidth(160)
        self.start_stop_button.setFixedHeight(40)
        self.start_stop_button.clicked.connect(self.start_stop)

        self.tempo_label = QLabel(str(self.tempo))
        self.tempo_label.setFont(QFont('Arial', 15))
        self.tempo_label.setStyleSheet("background-color: rgba(0, 255, 255, 90)")

        # layouts
        hbox = QHBoxLayout()
        hbox.addWidget(self.start_stop_button)
        hbox.addWidget(self.tempo_slider)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(self.tempo_label)

        self.setGeometry(820, 300, 300, 150)
        self.setLayout(vbox)
        self.setWindowTitle("Metronome")

    def start_stop(self):
        if self.is_running:
            self.timer.stop()
            self.is_running = False
            self.start_stop_button.setText("Start")
        else:
            self.timer.start(round(60000 / self.tempo))
            self.is_running = True
            self.start_stop_button.setText("Stop")

    def set_tempo(self, tempo):
        self.tempo = tempo
        self.tempo_label.setText(str(tempo))
        if self.is_running:
            self.start_stop()
            self.start_stop()

    def tick(self):
        winsound.Beep(1000, 200)

    def create_button(self, window):
        Menu_button("Metronome", window, self.x_cor, self.y_cor, self.wg, self.hg, self.on_click)

    def on_click(self):
        self.show()
