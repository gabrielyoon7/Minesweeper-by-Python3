import sys, pygame
from settings import *
from pygame.locals import *

class GUI():
    def __init__(self): #초기화
        pass
    def run(self):
        pygame.init() #pygame 초기화. 초기화를 해야 pygame을 사용할 수 있다고 함.
        self.screen = pygame.display.set_mode(SCREEN_SIZE) #디스플레이 크기 설정
        pygame.display.set_caption('Minesweeper') #프로그램 이름 설정
        while True:  # main game loop (게임에 필요한 메소드 불러오기)

            #필요한 함수를 여기에 다 전부 다 불러와야함.
            self.test() #불러와야 하는 함수는 모두 이런식으로 넣어야함. 예를들면 그래픽 출력 부분
            #게임 하면서 필요한 함수를 죄다 여기에 불러온다고 생각하면 편함.


            for event in pygame.event.get(): #창 안의 이벤트를 받는 영역. 예를 들면 종료키, 키보드키, 마우스 클릭 등
                if event.type == QUIT:#상단의 X키 누를 때 까지 프로그램 종료 안하고 유지하기 (필수임)
                    pygame.quit()
                    sys.exit()
            pygame.display.update()

    def test(self): #예시 보여주려고 넣은거니깐 삭제하거나 수정 바람.
        pass






