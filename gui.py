import sys, pygame
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QRadioButton, QWidget
from qtgui import QtGui
from settings import *
from pygame.locals import *
from gameLogic import GameLogic

class GUI(QWidget): #임시. pygame 안써도 됨.
    def __init__(self): #초기화
        pygame.init()  # pygame 초기화. 초기화를 해야 pygame을 사용할 수 있다고 함.
        super().__init__()
        self.count = 0
        self.screen = pygame.display.set_mode(SCREEN_SIZE)  # 디스플레이 크기 설정
        pygame.display.set_caption('Minesweeper')  # 프로그램 이름 설정
        level = BEGINNER
        GameLogic.createMap(self, level)
        while True:  # main game loop (게임에 필요한 메소드 불러오기)
            if pygame.event.type == QUIT:  # 상단의 X키 누를 때 까지 프로그램 종료 안하고 유지하기 (필수임)
                pygame.quit()
                sys.exit()
        self.difficulty()

        pygame.display.update()

    def draw_Cells(self, arr):
        CELL_SIZE = 50
        COLUMN_COUNT = len(arr[0])
        ROW_COUNT = len(arr)
        font = pygame.font.Font(None, 30)

        for column_index in range(COLUMN_COUNT):
            for row_index in range(ROW_COUNT):
                rect = (CELL_SIZE * column_index, CELL_SIZE * row_index, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, GRAY, rect)  # 커버
                pygame.draw.rect(self.screen, BLACK, rect, 1)

    def difficulty(self,arr):
        self.setGeometry(600, 200, 700, 700)
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel("지뢰찾기")
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
        self.on_clicked()
        self.draw_Cells(arr)

    def on_clicked(self):
        radio = self.sender()
        if radio.isChecked():
            self.label.setText(radio.text()+" 선택")
            print("checked " + radio.text())
