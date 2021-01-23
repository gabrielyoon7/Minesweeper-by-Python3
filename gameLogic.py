import random
from settings import *


class GameLogic():
    def __init__(self): #게임의 초기화 지점
        pass

    def run(self): # 실행 부분
        level= self.getLevel()
        map = self.createMap(level)
        self.DisplayMap(map) #콘솔 출력용. GUI랑은 상관 X

    def getLevel(self): #레벨 가져오기(나중에 수정 필요)
        while True:
            level = input("난이도를 입력하세요 (초보, 중급, 고급): ")
            if level=='초보':
                return BEGINNER
            if level=='중급':
                return INTERMEDIATE
            if level=='고급':
                return ADVANCED
            print("제대로 입력해주세요.")

    def createMap(self, level): #레벨에 따른 맵 생성 + 레벨에 따른 지뢰 심기 + 지뢰 근처에 적절한 숫자 생성 한번에 처리함.
        width = level[0]
        height = level[1]
        mine = level[2]
        arr = [[0 for row in range(width)] for column in range(height)]
        for num in range(mine):
            x = random.randint(0, width - 1) #지뢰의 x축 범위 랜덤으로 설정
            y = random.randint(0, height - 1) #지뢰의 y축 범위 랜덤으로 설정
            arr[y][x] = 'X' #생성된 지뢰 좌표에 X로 표현

            #지뢰 주변 힌트 숫자 생성
            if (x >= 0 and x <= width - 2) and (y >= 0 and y <= height - 1):
                if arr[y][x + 1] != 'X':
                    arr[y][x + 1] += 1  # center right
            if (x >= 1 and x <= width - 1) and (y >= 0 and y <= height - 1):
                if arr[y][x - 1] != 'X':
                    arr[y][x - 1] += 1  # center left
            if (x >= 1 and x <= width - 1) and (y >= 1 and y <= height - 1):
                if arr[y - 1][x - 1] != 'X':
                    arr[y - 1][x - 1] += 1  # top left
            if (x >= 0 and x <= width - 2) and (y >= 1 and y <= height - 1):
                if arr[y - 1][x + 1] != 'X':
                    arr[y - 1][x + 1] += 1  # top right
            if (x >= 0 and x <= width - 1) and (y >= 1 and y <= height - 1):
                if arr[y - 1][x] != 'X':
                    arr[y - 1][x] += 1  # top center
            if (x >= 0 and x <= width - 2) and (y >= 0 and y <= height - 2):
                if arr[y + 1][x + 1] != 'X':
                    arr[y + 1][x + 1] += 1  # bottom right
            if (x >= 1 and x <= width - 1) and (y >= 0 and y <= height - 2):
                if arr[y + 1][x - 1] != 'X':
                    arr[y + 1][x - 1] += 1  # bottom left
            if (x >= 0 and x <= width - 1) and (y >= 0 and y <= height - 2):
                if arr[y + 1][x] != 'X':
                    arr[y + 1][x] += 1  # bottom center
        return arr

    def DisplayMap(self, map): #콘솔 출력용 (GUI랑은 상관 없음)
        for row in map:
            print(" ".join(str(cell) for cell in row))
            print("")
