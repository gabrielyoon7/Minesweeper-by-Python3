import sys, pygame
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QRadioButton, QWidget
from PyQt5 import QtGui
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
        arr = GameLogic.createMap(self, level)#맵을 생성하고 저장
        OPENED = [[False for row in range(len(arr))] for column in range(len(arr[0]))]
        while True:  # main game loop (게임에 필요한 메소드 불러오기)
            if pygame.event.type == QUIT:  # 상단의 X키 누를 때 까지 프로그램 종료 안하고 유지하기 (필수임)
                pygame.quit()
                sys.exit()
            self.difficulty()
            if pygame.event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.event.button == 1:  # 마우스 왼쪽 클릭시
                    column_index = pygame.event.pos[0] // CELL_SIZE
                    row_index = pygame.event.pos[1] // CELL_SIZE
                    if arr[column_index][row_index] == 'X':  # 선택된 칸이 X이면 종료, (오류)선택해도 자꾸 open_Cell 함수로 넘어감
                        return
                '''else:  # 선택된 칸 오픈
                    self.open_Cell(arr, column_index, row_index)'''
            self.draw_Cells(arr)  # 칸 그리기
        pygame.display.update()

    def draw_Cells(self, arr):
        COLUMN_COUNT = len(arr[0])
        ROW_COUNT = len(arr)

        for column_index in range(COLUMN_COUNT):
            for row_index in range(ROW_COUNT):
                rect = (CELL_SIZE * column_index, CELL_SIZE * row_index, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, GRAY, rect)
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

    """
    def open_Cell(self,arr,col,row):
        if col < 0 or col >= len(arr) or row < 0 or row >= len(arr[0]):
            return
        cell = arr[col][row]  # 선택된 칸
        if OPENED[col][row]: #이미 확인한 칸 여기서 자꾸 오류 생김
            return
        OPENED[col][row] = True

        if cell > 0:#숫자 나오게 함
            rect = (CELL_SIZE * col, CELL_SIZE * row, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(self.screen, CYAN, rect)
        elif cell == 0: #셀이 0이면 1 이상의 수가 나올때까지 반복해서 여는 재귀함수 생성 / for 문으로 고쳐야할 듯
            self.open_Cell(col + 1, row)
            self.open_Cell(col, row + 1)
            self.open_Cell(col + 1, row + 1)
            self.open_Cell(col - 1, row)
            self.open_Cell(col, row - 1)
            self.open_Cell(col - 1, row - 1)
            self.open_Cell(col + 1, row - 1)
            self.open_Cell(col - 1, row + 1)
            """