from classes.Board import Board
from classes.Player import HumanPlayer, ComputerPlayer


board = Board(3, 3, ComputerPlayer("#"), ComputerPlayer("£"))
# board.addLine(0, 0, 0, 1, "@")
# board.addLine(0, 1, 0, 2, "@")
# board.addLine(0, 0, 1, 0, "@")
board.play()
