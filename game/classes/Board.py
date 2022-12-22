"""
Board, class of sdpa-game
Alex (Lexi) Beavil 2022
@aeroniemi

Contains all of the "play" features of the dots and boxes game
"""


import random
import time
from classes.Player import Player, RandomPlayer, ComputerPlayer, HumanPlayer
from classes.Move import Move


class Board ():
    def __init__(self, width=3, height=3, player1=False, player2=False):
        """
        Takes optional args:
        - width (int)
        - height (int)
        - player1 (Player)
        - player2 (Player)
        Args not required if using Board.initialise()
        """
        if not (type(width) is int and type(height) is int):
            raise TypeError("Board dimensions should be int")
        if width < 2 or height < 2:
            raise Exception("Board size must be greater than 2x2")
        self.width = width
        self.height = height
        self.build()
        self.players = [player1, player2]
        self.activePlayer = 0
        self.moves = 1
        self.showMoves = False

    def initialise(self):
        """
        Runs interactive settings, then redirects the player to actually play
        the game.
        """
        print("Game Settings")
        self.showMoves = self.settingInput("Show Possible moves and ratings?")
        self.width = self.sizeInput("Width of the board:", 3)
        self.height = self.sizeInput("Height of the board:", 3)
        self.players[0] = HumanPlayer("A")
        if self.settingInput("Human Opponent?"):
            self.players[1] = HumanPlayer("B")
        elif self.settingInput("Random Computer Opponent?"):
            self.players[1] = RandomPlayer("B")
        else:
            self.players[1] = ComputerPlayer("B")
        print("Let's Play")
        self.build()  # we must rebuild the board as the size might have changed
        time.sleep(2)
        self.play()

    def settingInput(self, text):
        """
        Manages a boolean entry on behalf of initialise
        text - str, the descriptor text
        """
        res = input(f"{text} (y/n) ")
        if res == "y" or res == "yes":
            return True
        return False

    def sizeInput(self, text, default):
        """
        Manages a width/height entry on behalf of initialise
        text - str, the descriptor text
        default - int, the default value to return if no user input
        """
        res = input(f"{text} ({default}) ")
        if res == "":
            return default
        if (not res.isdigit()) or int(res) < 3 or int(res) > 20:
            # I indented it because it looked pretty
            print("    Invalid input, must be integer in range 3-20")
            return self.sizeInput(text)
        return int(res)

    def build(self):
        """
        'builds' the board for initialisation
        horizontal then vertical as that's how we draw it
        y is inverted, both axis start from 0
        """
        self.grid = []
        # the total number of cells in each dimension is 2 * possible lines + 1
        # iterate vertically, and just make a blank grid of the right size
        for i in range(0, (self.height*2)+1):
            self.grid.append([" "]*((self.width*2)+1))
        # now we have the grid, let's fill it with dots in the right places
        for i, row in enumerate(self.grid):
            for j in range(len(row)):
                if i % 2 == 0:
                    if j % 2 == 0:
                        row[j] = "●"

    def draw(self):
        """
        Draw the board to the CLI
        """
        # print the horizontal 1 2 3 thing
        print("  "+" ".join(str(i) for i in range(0, self.width+1)))
        # loop vertically over the grid
        for i in range(len(self.grid)):
            s = ""
            if i % 2 == 0:  # even row, so it's got dots on it
                s += str(i // 2) + " "  # add the y axis id
                for cell in self.grid[i]:  # loop horizontally
                    # if it's Player then draw a line, if not, just print the text
                    if isinstance(cell, Player):
                        s += "━"
                    else:
                        s += cell
            else:  # odd row, so just lines and box centres
                s += "  "
                for j in range(len(self.grid[i])):  # loop horizontally
                    cell = self.grid[i][j]
                    if isinstance(cell, Player):  # if the cell is Player
                        if j % 2 == 0:  # and even, draw a line
                            s += "┃"
                        else:  # and odd, draw the charachter as it's a box centre
                            s += cell.getIcon()
                    else:  # probably blank
                        s += cell
            print(s)  # draw that line finally

    def validateMove(self, x1, y1, x2, y2):
        """
        Is this line a valid move?
        Gives Exceptions that must be handled by the validating agent
        """
        row, col = self.getCell(
            x1, y1, x2, y2)  # could raise a not contiguous error, to be caught by validating agent
        if row > len(self.grid)-1:
            raise Exception(
                f"Move is outside of vertical bounds: {x1,y1,x2,y2}")
        if col > len(self.grid[row]):
            raise Exception(
                f"Move is outside of horizontal bounds: {x1,y1,x2,y2}")
        if self.grid[row][col] != " ":
            raise Exception(
                f"Line already exists in this cell: {x1,y1,x2,y2}")
        # if it's a valid move, return True
        return True

    def addLine(self, x1, y1, x2, y2, player):
        """
        Add a move to the board if it's valid
        Extra check on entries to stop later errors
        """
        try:
            self.validateMove(x1, y1, x2, y2)
        except:
            raise
        # if the move is good, add it to the board
        self.setLine(x1, y1, x2, y2, player)

    def getCell(self, x1, y1, x2, y2):
        """
        Find out what cell in the grid this line would occupy
        """
        # check whether the pythagorean distance is 1, which guarantees this is a contiguous move
        if ((x1-x2)**2 + (y1-y2)**2)**0.5 != 1:
            raise Exception(f"Move is not contiguous: {x1,y1,x2,y2}")

        # normalise the coordinates so that 1 is closer to the start of the board than 2
        row = y1*2 if y1 == y2 else min(y1, y2)*2+1
        col = x1*2 if x1 == x2 else min(x1, x2)*2+1
        return row, col

    def setLine(self, x1, y1, x2, y2, player):
        """
        Put the line on the board
        Doesn't error check, assumes this was done upstream (e.g. by Board.addLine())
        """
        row, col = self.getCell(x1, y1, x2, y2)
        self.grid[row][col] = player
        return True

    def whoGoesFirst(self):
        """
        Randomly decide which user goes first
        """
        res = random.random()
        if res > 0.5:
            return 1
        return 0

    def getPrettyPlayer(self):
        """
        Make a pretty string for the active player
        """
        return f"{self.getActivePlayer().getIcon()}'s"

    def getActivePlayer(self):
        """
        Return the active Player object
        """
        return self.players[self.activePlayer]

    def getLegalMoves(self):
        """
        Return a list of all of the legal moves still remaining, as Move objects
            Iterates over all possible x1,y1 start coordinates and tests the lines
            right and down from them
        """
        legalMoves = []
        for y1 in range(0, self.height+1, 1):
            for x1 in range(0, self.width+1, 1):
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
        """
        Work out if the last move scored any new points
            If it did, add those points to the player and show the box as filled in the grid
        """
        for j in range(1, len(self.grid), 2):
            for i in range(1, len(self.grid[j]), 2):
                # top, right, bottom, left
                if self.grid[i][j] == " ":
                    edges = (self.grid[i][j-1], self.grid[i+1]
                             [j], self.grid[i][j+1], self.grid[i-1][j])
                    if not " " in edges:
                        self.grid[i][j] = self.getActivePlayer()
                        self.getActivePlayer().addPoints()
                        return

    def getMaxNumberOfMoves(self):
        """
        Return the maximum possible number of moves (and thus the end move of the game)
        The max number of edges is 2ab+a+b because maths (expansion of (2a+1)*(2b+1)-(ab)-((a+1)*(b+1))
        """
        return (2*self.width*self.height)+self.width+self.height

    def printPoints(self):
        """
        Print the current points table in a pretty fashion
        """
        print(
            f"Player {self.players[0].getIcon()}: {self.players[0].getPoints()}   Player {self.players[1].getIcon()}: {self.players[1].getPoints()}")

    def printWinner(self):
        """
        Once we reach the end of the game, print a winner statement
        """
        player1 = self.players[0].getPoints()
        player2 = self.players[1].getPoints()
        if player1 == player2:
            print("It's a tie")
        if player1 > player2:
            print(f"Player {self.players[0].getIcon()} Wins")
        if player1 < player2:
            print(f"Player {self.player[1].getIcon()} Wins")

    def printMoves(self):
        """
        Print a list of all of the valid moves this turn
            Primarily for debugging the rating/legal move generator, but also useful
            if you're incompetent at the game like me
            Can be enabled in initalise()
        """
        print("Valid moves:")
        possibleMoves = self.getLegalMoves()
        possibleMoves = sorted(possibleMoves, key=lambda move: (
            move.rate(self), random.random()), reverse=True)
        for move in possibleMoves:
            move.draw(self)

    def play(self):
        """
        The "play" loop, responsible for actually running a game
        """
        # check we have 2 players, as this is quite hard if we don't
        if not isinstance(self.players[0], Player) or not isinstance(self.players[1], Player):
            raise Exception(
                "Not enough Player present, check you're launching the game properly")

        # determine who goes first
        self.activePlayer = self.whoGoesFirst()

        # tell the people the result
        print(
            f"The coin was flipped, and player {self.getActivePlayer().getIcon()} goes first")

        # play the game until there are no possible moves left
        while self.moves <= self.getMaxNumberOfMoves():
            print(
                f"It's player {self.getPrettyPlayer()} turn; turn number {self.moves}")
            self.draw()

            # if you enabled move display, do that here
            if self.showMoves:
                self.printMoves()

            # take entry from the user
            # it's a loop as py gets sad if you use recursion too much (such as happens when the random player just keeps trying stuff)
            while True:
                entry = self.getActivePlayer().input(self)
                if entry == True:
                    break
            # now the user has submitted their input, deal with points, then flip the user
            self.calculatePoints()
            self.printPoints()
            self.activePlayer ^= 1  # bitwise way of flipping 1 for 0
            self.moves += 1
        # the game has finished, let's show the people how it ended
        print("\n\n\n\n\n\n\n\n")
        print("The Game is complete")
        print("Winning board:")
        self.draw()
        self.printPoints()
        self.printWinner()
