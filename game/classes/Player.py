import re
import random
import time


class Player:
    def __init__(self, icon):
        self.icon = icon or "@"
        self.points = 0
        # self.board = board

    def addLine(self, x1, y1, x2, y2):
        return self.board(x1, y1, x2, y2, self)

    def getIcon(self):
        return self.icon

    def input(self):
        return

    def __str__(self):
        """Used for displaying the icon by the board drawer"""
        return self.getIcon()

    def __int__(self):
        """Used for easy access to the points by win calculator"""
        return self.getPoints()

    def addPoints(self):
        self.points += 1

    def setPoints(self, points):
        self.points = points or 0

    def getPoints(self):
        return self.points or 0


class RandomPlayer(Player):
    def input(self, board):
        time.sleep(2)
        x1 = random.randint(0, board.width)
        y1 = random.randint(0, board.height)
        if bool(random.getrandbits(1)) == True:
            x2 = x1+1
            y2 = y1
        else:
            x2 = x1
            y2 = y1+1
        valid = False
        try:
            board.validateMove(x1, y1, x2, y2)
        except:
            return False
        else:
            board.addLine(x1, y1, x2, y2, self)
            print(f"Computer player has added line: {x1,y1,x2,y2}")
            return True


class ComputerPlayer(Player):
    def input(self, board):
        time.sleep(2)
        possibleMoves = board.getLegalMoves()
        possibleMoves = sorted(possibleMoves, key=lambda move: (
            move.rate(board), random.random()), reverse=True)
        x1, y1, x2, y2 = possibleMoves[0].getXY()
        board.addLine(x1, y1, x2, y2, self)
        print(f"Computer player has added line: {x1,y1,x2,y2}")
        return True


class HumanPlayer(Player):
    def input(self, board):
        print("Enter your line in the format 'x1,y1,x2,y2'")
        instr = input()
        matched = re.findall("(\d+),(\d+),(\d+),(\d+)", instr)
        if len(matched) != 1:
            print("Invalid input - check format")
            return self.input(board)
        x1, y1, x2, y2 = map(int, matched[0])
        try:
            board.addLine(x1, y1, x2, y2, self)
        except Exception as e:
            print(f"Move invalid: {e}")
            print(f"Try again")
            self.input(board)
        # print(x1, y1, x2, y2)
        return True
