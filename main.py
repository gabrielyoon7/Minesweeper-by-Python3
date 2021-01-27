# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import gui, gameLogic, gui_Intro

# Press the green button in the gutter to run the script.
class Minesweeper:
    def run(self):
#        gui_Intro.Window()
        gui.GUI() #GUI 불러오기
#        gameLogic.GameLogic().run() #게임 로직 불러오기

#이 프로그램의 시작점
if __name__ == '__main__':
    Minesweeper().run()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
