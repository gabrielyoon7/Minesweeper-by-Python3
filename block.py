from settings import *
#블럭에 관한 정의
class Block():
    blocks = [  # 블럭 모양에 대한 정의 (4x4크기고, 각 리스트 안에 리스트로 회전하는 경우를 모두 넣어서 전환할 수 있게 처리)
        [[1, 5, 9, 13], [4, 5, 6, 7]],  # 모양1
        [[4, 5, 9, 10], [2, 6, 5, 9]],  # 모양2
        [[6, 7, 9, 10], [1, 5, 6, 10]],  # 모양3
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],  # 모양3
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],  # 모양4
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],  # 모양5
        [[1, 2, 5, 6]],  # 모양6
    ]
    color = [WHITE, RED, GREEN, BLUE, ORANGE, GOLD, PURPLE, CYAN, BLACK, GRAY]  # 블럭 색상. settings에서 값을 가져옴

    def __init__(self): #초기화
        pass

    def newBlock(self): #블럭 생성
        self.blocks = Block()

    def drawBlock(self): #임시
        return self.blocks[1][0]

    def rotateBlock(self):
        pass

    def moveHorizontal(self):
        pass


#블럭 크기
#블럭 회전
