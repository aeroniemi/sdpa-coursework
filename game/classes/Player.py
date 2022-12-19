import re


class Player:
    def __init__(self, icon):
        self.icon = icon or "@"
        # self.board = board

    def addLine(self, x1, y1, x2, y2):
        return self.board(x1, y1, x2, y2, self)

    def getIcon(self):
        return self.icon

    def input(self):
        return


class ComputerPlayer(Player):
    def input(self):
        return


class HumanPlayer(Player):
    def input(self, board):
        print("Enter your line in the format 'x1,y1,x2,y2'")
        instr = input()
        matched = re.findall("(\d+),(\d+),(\d+),(\d+)", instr)
        if len(matched) != 1:
            print("Invalid input - check format")
            self.input(board)
        x1, y1, x2, y2 = map(int, matched[0])
        # try:
        board.addLine(x1, y1, x2, y2, self)
        # except:
        #     print("The line you entered is invalid, try again")
        #     self.input(board)
        print(x1, y1, x2, y2)
        return True
