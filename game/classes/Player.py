"""
Player, class of sdpa-game
Alex (Lexi) Beavil 2022
@aeroniemi

Contains features associated with players, including the children:
    HumanPlayer
    RandomPlayer
    ComputerPlayer
"""

import re
import random
import time


class Player:
    def __init__(self, icon):
        self.icon = icon or "@"
        self.points = 0
        # self.board = board

    def getIcon(self):
        """
        Get the player's text icon (usually 'A' or 'B')
        """
        return self.icon

    # def __str__(self):
    #     """
    #     Used for displaying the icon by the board drawer
    #     """
    #     return self.getIcon()

    # def __int__(self):
    #     """
    #     Used for easy access to the points by win calculator
    #     """
    #     return self.getPoints()

    def addPoints(self, points=1):
        """
        Add a point to the player
        """
        self.points += points

    def setPoints(self, points):
        """
        Set the points of the player
        Useful for resetting points if needd
        """
        self.points = points or 0

    def getPoints(self):
        """
        How many points does this player have?
        """
        return self.points or 0


class RandomPlayer(Player):
    """
    Extends Player
    Give a random line as response
        Kinda like a dumb AI player
        It just randomly tries lines until it gets a valid one
        It's also useful for testing entry conditions
    """

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
    """
    Extends Player
    Gives a smart response
        It looks at the available moves, and picks the best
    """

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
    """
    Extends Player
    Takes input from a human on the CLI
    """

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
