import sys, pygame

import gameLogic
from settings import *
from pygame.locals import *
from gameLogic import GameLogic
# 내 생각에는 일단 " "(스페이스 한칸)로 채워져 있는 판을 만들고, 해당 칸을 클릭했을 때, map에 있는 해당 칸으로 바꿔주는게 어떨까 싶음.

class GUI(): #임시. pygame 안써도 됨.
    def __init__(self, level): #초기화
        pygame.init()  # pygame 초기화. 초기화를 해야 pygame을 사용할 수 있다고 함.
        super().__init__()
        SCREEN_SIZE=self.getScreenSize(level)
        SCREEN_WIDTH = self.getScreenSize(level)[0]
        SCREEN_HEIGHT = self.getScreenSize(level)[1]
        num = 0
        self.count = 0
        self.screen = pygame.display.set_mode(SCREEN_SIZE)  # 디스플레이 크기 설정
        pygame.display.set_caption('Minesweeper')  # 프로그램 이름 설정
        gameLevel=self.getLevel(level) #레벨을 tuple 형태로 받아옴.
        arr = GameLogic.createMap(self, gameLevel) #맵을 생성하고 저장
        OPENED = [[False for row in range(len(arr))] for column in range(len(arr[0]))]
        self.draw_Cells(arr)  # 칸 그리기

        while True:  # main game loop (게임에 필요한 메소드 불러오기)
            for event in pygame.event.get(): #창 안의 이벤트를 받는 영역. 예를 들면 종료키, 키보드키, 마우스 클릭 등
                if event.type == QUIT:#상단의 X키 누를 때 까지 프로그램 종료 안하고 유지하기 (필수임)
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # 마우스 왼쪽 클릭시
                        column_index = event.pos[0] // CELL_SIZE
                        row_index = event.pos[1] // CELL_SIZE
                        print(column_index, row_index)
                        if arr[column_index][row_index] == 'X':  # 선택된 칸이 X이면 종료, (오류)선택해도 자꾸 open_Cell 함수로 넘어감
                            self.open_All(arr, OPENED)
                            print("패배")
                            fail_font = pygame.font.SysFont('malgungothic', 70)
                            fail_image = fail_font.render('패배', True, RED)
                            self.screen.blit(fail_image, fail_image.get_rect(centerx=SCREEN_WIDTH // 2,centery=SCREEN_HEIGHT // 2))
                        else:  # 선택된 칸 오픈
                            arr=self.open_Cell(arr,OPENED, column_index, row_index)
                    elif event.button == 3: # 마우스 우클릭시 깃발
                        column_index = event.pos[0] // CELL_SIZE
                        row_index = event.pos[1] // CELL_SIZE
                        flag_font = pygame.font.SysFont('malgungothic', 30)
                        flag_image = flag_font.render('V', True, WHITE)
                        self.screen.blit(flag_image, (column_index * CELL_SIZE + 10, row_index * CELL_SIZE + 10))
                        while num>4: # 승리표시가 되는지 확실히 모르겠음
                            if GameLogic().createMap(self) == arr[column_index][row_index]:
                                num+=1
                                continue
                            success_font = pygame.font.SysFont('malgungothic', 70)
                            success_image = success_font.render('승리', True, RED)
                            self.screen.blit(success_image,success_image.get_rect(centerx=SCREEN_WIDTH // 2, centery=SCREEN_HEIGHT // 2))
#               self.draw_Cells(arr)  # 칸 그리기
            pygame.display.update()

    def getLevel(self, level): #레벨 가져오기(나중에 수정 필요)
        if level=='초급':
            return BEGINNER
        elif level=='중급':
            return INTERMEDIATE
        elif level=='고급':
            return ADVANCED

    def getScreenSize(self,level):
        if level=='초급':
            return SCREEN_SIZE_BEGINNER
        elif level=='중급':
            return SCREEN_SIZE_INTERMEDIATE
        elif level=='고급':
            return SCREEN_SIZE_ADVANCED


    def draw_Cells(self, arr):
        COLUMN_COUNT = len(arr[0])
        ROW_COUNT = len(arr)

        for column_index in range(COLUMN_COUNT):
            for row_index in range(ROW_COUNT):
                rect = (CELL_SIZE * column_index, CELL_SIZE * row_index, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, GRAY, rect)
                pygame.draw.rect(self.screen, BLACK, rect, 1)

    def open_Cell(self,arr,OPENED,col,row):

        print("open_Cell is running1")
        if col < 0 or col >= len(arr) or row < 0 or row >= len(arr[0]):
            print("open_Cell is running2")
            return arr
        print("open_Cell is running3")
        cell = arr[col][row]  # 선택된 칸
        print("open_Cell is running4")
        if OPENED[col][row]: #이미 확인한 칸 여기서 자꾸 오류 생김
            print("open_Cell is running5")
            return arr
        print("open_Cell is running6")
        OPENED[col][row] = True
        print("open_Cell is running7")
        if cell == 0: #셀이 0이면 1 이상의 수가 나올때까지 반복해서 여는 재귀함수 생성 / for 문으로 고쳐야할 듯
            print("open_Cell is running8")
            self.open_Cell(arr, OPENED, col + 1, row)
            self.open_Cell(arr, OPENED,col, row + 1)
            self.open_Cell(arr, OPENED,col + 1, row + 1)
            self.open_Cell(arr, OPENED,col - 1, row)
            self.open_Cell(arr, OPENED,col, row - 1)
            self.open_Cell(arr, OPENED,col - 1, row - 1)
            self.open_Cell(arr, OPENED,col + 1, row - 1)
            self.open_Cell(arr, OPENED,col - 1, row + 1)
        print("open_Cell is running9")
        font5 = pygame.font.SysFont('notosanscjkkrblack', 50)
        print("open_Cell is running10")
        img5 = font5.render(str(cell), True, BLACK)
        print("open_Cell is running11")
        self.screen.blit(img5, (CELL_SIZE*col+10, CELL_SIZE*row+10))
        return arr

    def open_All(self,arr,OPENED):
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                self.open_Cell(arr,OPENED,i,j)
