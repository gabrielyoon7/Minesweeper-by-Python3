from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QRadioButton, QWidget
from PyQt5 import QtGui
#
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
import sys, gui

#첫 난이도를 정하는 부분.
#여기에서 난이도를 gui로 넘겨야 할 것 같음.

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

        #임시버튼
        # GUI를 실행하는 임시 버튼 (나중에는 이 화면에서 선택된 난이도를 같이 gui로 넘겨줘야 할 듯)
        btnRun = QPushButton("GUI 실행하기 (임시)", self)  # 버튼 텍스트
        btnRun.move(20, 20)  # 버튼 위치
        btnRun.clicked.connect(self.btnRun_clicked)  # 클릭 시 실행할 function

    def btnRun_clicked(self): #버튼을 눌렀을 때 gui 실행
        gui.GUI("초급") #여기에 난이도를 주면 gui에서 맵을 자동으로 생성함. 라디오 버튼으로 받은걸 넘겨줄 수 있도록 설계하면 좋을 것 같음.


    def on_clicked(self):
        radio = self.sender()
        if radio.isChecked():
            self.label.setText(radio.text()+" 선택")
            print("checked " + radio.text())


app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())