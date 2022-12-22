"""
main, entry point to sdpa-game
Alex (Lexi) Beavil 2022
@aeroniemi

Imports classes and launches the game
"""
# imports
from classes.Board import Board

"""
The usual way of launching the game, including the initialisation routine
"""
board = Board(3, 3)
board.initialise()

"""
For testing purposes a different launch method exists that bypasses settings, and allows you to add lines as-you-wish.
Useful for easily reproducing test scenarios
"""
# from classes.Player import HumanPlayer, RandomPlayer, ComputerPlayer
# a = HumanPlayer("A")
# board = Board(3, 3, a, ComputerPlayer("B"))
# board.addLine(1, 1, 1, 0, a)
# board.addLine(0, 0, 1, 0, a)
# board.addLine(0, 1, 1, 1, a)
# board.play()
