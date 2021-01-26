from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.initialize()

    def initialize(self):
        self.setGeometry(700, 300, 500, 400)
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel("Minesweeper")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QtGui.QFont('Hack', 15))
        layout.addWidget(self.label)

        self.radioButton = QRadioButton("초급")
        self.radioButton.setChecked(True)
        self.radioButton.setFont(QtGui.QFont('Hack', 15))
        self.radioButton.toggled.connect(self.on_clicked)
        layout.addWidget(self.radioButton)

        self.radioButton = QRadioButton("중급")
        self.radioButton.setChecked(False)
        self.radioButton.setFont(QtGui.QFont('Hack', 15))
        self.radioButton.toggled.connect(self.on_clicked)
        layout.addWidget(self.radioButton)

        self.radioButton = QRadioButton("고급")
        self.radioButton.setChecked(False)
        self.radioButton.setFont(QtGui.QFont('Hack', 15))
        self.radioButton.toggled.connect(self.on_clicked)
        layout.addWidget(self.radioButton)

    def on_clicked(self):
        radio = self.sender()
        if radio.isChecked():
            self.label.setText(radio.text()+" 선택")
            print("checked " + radio.text())


app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())