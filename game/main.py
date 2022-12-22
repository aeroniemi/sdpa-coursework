from classes.Board import Board
from classes.Player import HumanPlayer, RandomPlayer, ComputerPlayer

a = HumanPlayer("A")
board = Board(3, 3, a, ComputerPlayer("B"))
# board.addLine(1, 1, 1, 0, a)
# board.addLine(0, 0, 1, 0, a)
# board.addLine(0, 1, 1, 1, a)
board.play()
