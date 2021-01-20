# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys, pygame, block
from settings import *
from pygame.locals import *

# Press the green button in the gutter to run the script.
class Tetris:
    def __init__(self, garoBlock, seroBlock): #초기화 지점
        self.width = garoBlock*BWIDTH  #플레이 영역 가로줄 길이 = 블럭 16개 길이를 의미
        self.height = seroBlock*BHEIGHT  #플레이 영역 세로줄 길이 = 블럭 30개 길이를 의미

        # Rect(x좌표, y좌표, 가로길이, 세로길이) 단, 가로길이와 세로길이 둘 중 하나는 두께 값임.
        # 경계선 한줄 한줄을 사각형으로 그림 (그려진 사각형 배치는 drawPlayBorder에서 함)
        self.borderUp = pygame.Rect(X, Y, self.width, THICKNESS)
        self.borderLeft = pygame.Rect(X, Y, THICKNESS, self.height)
        self.borderDown = pygame.Rect(X, Y + self.height, self.width, THICKNESS)
        self.borderRight = pygame.Rect(X + self.width - THICKNESS, Y, THICKNESS, self.height)

    def run(self):
        pygame.init() #pygame 초기화. 초기화를 해야 pygame을 사용할 수 있다고 함.
        self.screen = pygame.display.set_mode(SCREEN_SIZE) #디스플레이 크기 설정
        pygame.display.set_caption('Tetris') #프로그램 이름 설정
        blockObject = block.Block()
        while True:  # main game loop (게임에 필요한 메소드 불러오기)
            #게임 로직 실행 (미구현)

            self.showGame() #그래픽 실행

            if blockObject.blocks is not None: #임시로 아무 블럭 하나 그려보려고 했는데 실패함.
                for i in range(4):
                    for j in range(4):
                        p = i * 4 + j
                        if p in blockObject.drawBlock():
                            pygame.draw.rect(self.screen, blockObject.color[1],
                                             [X+ self.width/2,
                                              Y,
                                              20, 20])

            for event in pygame.event.get():
                if event.type == QUIT:#상단의 X키 누를 때 까지 프로그램 종료 안하고 유지하기
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN: #키 등록
                    if event.key == pygame.K_UP:
                        print("UP")
                    if event.key == pygame.K_DOWN:
                        print("DOWN")
                    if event.key == pygame.K_LEFT:
                        print("LEFT")
                    if event.key == pygame.K_RIGHT:
                        print("RIGHT")
            pygame.display.update()

    def showGame(self): #그래픽 실행.
        self.screen.fill(WHITE) #배경
        self.drawPlayBorder() #게임 영역 그리기
        self.drawScoreBoard() #우측 점수 영역 그리기

    def drawPlayBorder(self): #블럭이 움직일 수 있는 경계선 그리기
        pygame.draw.rect(self.screen,BLACK,self.borderUp)
        pygame.draw.rect(self.screen,BLACK,self.borderDown)
        pygame.draw.rect(self.screen,BLACK,self.borderLeft)
        pygame.draw.rect(self.screen,BLACK,self.borderRight)

    def drawScoreBoard(self): #현재 점수 표시하는 영역(미완성)
        pass

#이 프로그램의 시작점
if __name__ == '__main__':
    Tetris(16,30).run()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
