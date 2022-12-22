import random
from classes.Player import Player
from classes.Move import Move


class Board ():
    def __init__(self, width, height, player1, player2):
        """
        @width: int, number of boxes in X axis
        @height: int, number of boxes in Y axis
        """
        if not (type(width) is int and type(height) is int):
            raise TypeError("Board dimensions should be int")
        if width < 2 or height < 2:
            raise Exception("Board size must be greater than 2x2")
        self.width = width
        self.height = height
        self.build()
        self.players = (player1, player2)
        self.activePlayer = 0
        self.moves = 1

    def build(self):
        """
        horizontal then vertical as that's how we draw it
        y is inverted, both axis start from 0
        """
        self.grid = []
        # the total number of cells in each dimension is 2 * possible lines + 1
        for i in range(0, (self.height*2)+1):
            self.grid.append([" "]*((self.width*2)+1))
        for i, row in enumerate(self.grid):
            for j in range(len(row)):
                if i % 2 == 0:
                    if j % 2 == 0:
                        row[j] = "●"

    def draw(self):
        # print("Drawing Board")
        print("  "+" ".join(str(i) for i in range(0, self.width+1)))
        for i in range(len(self.grid)):
            s = ""
            if i % 2 == 0:
                s += str(i // 2) + " "
                for cell in self.grid[i]:
                    if isinstance(cell, Player):
                        s += "━"
                    else:
                        s += cell
            else:
                s += "  "
                for j in range(len(self.grid[i])):
                    cell = self.grid[i][j]
                    if isinstance(cell, Player):
                        if j % 2 == 0:
                            s += "┃"
                        else:
                            s += str(cell)
                    else:
                        s += cell
            print(s)

    def validateMove(self, x1, y1, x2, y2):
        row, col = self.getCell(x1, y1, x2, y2)
        if row > len(self.grid)-1:
            raise Exception(
                f"Move is outside of vertical bounds: {x1,y1,x2,y2}")
        if col > len(self.grid[row]):
            raise Exception(
                f"Move is outside of horizontal bounds: {x1,y1,x2,y2}")
        if self.grid[row][col] != " ":
            raise Exception(
                f"Line already exists in this cell: {x1,y1,x2,y2}")
        return True

    def addLine(self, x1, y1, x2, y2, player):
        try:
            self.validateMove(x1, y1, x2, y2)
        except:
            raise
        self.setLine(x1, y1, x2, y2, player)
        

    def getCell(self, x1, y1, x2, y2):
        if ((x1-x2)**2 + (y1-y2)**2)**0.5 != 1:
            raise Exception(f"Move is not contiguous: {x1,y1,x2,y2}")
        row = y1*2 if y1 == y2 else min(y1, y2)*2+1
        col = x1*2 if x1 == x2 else min(x1, x2)*2+1
        return row, col

    def setLine(self, x1, y1, x2, y2, player):
        row, col = self.getCell(x1, y1, x2, y2)
        self.grid[row][col] = player
        return True

    def whoGoesFirst(self):
        res = random.random()
        if res > 0.5:
            return 1
        return 0

    def getPrettyPlayer(self):
        return f"{self.activePlayer+1}'s"

    def getActivePlayer(self):
        return self.players[self.activePlayer]

    def getLegalMoves(self):
        legalMoves = []
        for y1 in range(0, self.height, 1):
            for x1 in range(0, self.width, 1):
                try:
                    self.validateMove(x1, y1, x1+1, y1)
                except:
                    pass
                else:
                    legalMoves.append(Move(x1, y1, x1+1, y1))

                try:
                    self.validateMove(x1, y1, x1, y1+1)
                except:
                    pass
                else:
                    legalMoves.append(Move(x1, y1, x1, y1+1))
        return legalMoves

    def calculatePoints(self):
        for j in range(1, len(self.grid), 2):
            for i in range(1, len(self.grid[j]), 2):
                # top, right, bottom, left
                edges = (self.grid[i][j-1], self.grid[i+1]
                         [j], self.grid[i][j+1], self.grid[i-1][j])
                if len(set(edges)) == 1:
                    print(edges[0])
                    if isinstance(edges[0], Player):
                        self.grid[i][j] = edges[0]
                        edges[0].addPoints()

    def getMaxNumberOfMoves(self):
        # the max number of edges is 2ab+a+b because maths (expansion of (2a+1)*(2b+1)-(ab)-((a+1)*(b+1))
        return (2*self.width*self.height)+self.width+self.height

    def printPoints(self):
        print(
            f"Player 1: {self.players[0].getPoints()}   Player 2: {self.players[1].getPoints()}")

    def printWinner(self):
        player1 = self.players[0].getPoints()
        player2 = self.players[1].getPoints()
        if player1 == player2:
            print("It's a tie")
        if player1 > player2:
            print("Player 1 Wins")
        if player1 < player2:
            print("Player 2 Wins")

    def play(self):
        self.activePlayer = self.whoGoesFirst()
        print(f"{self.activePlayer+1} goes first")

        while self.moves <= self.getMaxNumberOfMoves():
            print(
                f"It's player {self.getPrettyPlayer()} turn; turn number {self.moves}")
            self.draw()
            print("Valid moves:")
            for move in self.getLegalMoves():
                move.draw(self)
            while True:
                entry = self.getActivePlayer().input(self)
                if entry == True:
                    break
            self.calculatePoints()
            self.printPoints()
            self.activePlayer ^= 1  # bitwise way of flipping 1 for 0
            self.moves += 1
        print("\n\n\n\n\n\n\n\n")
        print("The Game is complete")
        print("Winning board:")
        self.draw()
        self.printPoints()
        self.printWinner()
