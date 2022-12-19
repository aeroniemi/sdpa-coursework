import re


class Player:
    def __init__(self, board, icon):
        self.icon = icon or "@"
        self.board = board

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
    def input(self):
        print("Enter your line in the format 'x1,y1,x2,y2'")
        instr = input()
        matched = re.findall("(\d+),(\d+),(\d+),(\d+)", instr)
        if len(matched) != 1:
            print("Invalid input - check format")
            self.input()
        x1, y1, x2, y2 = matched[0]
        print(x1, y1, x2, y2)
