class Move:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self):
        return f"({self.x1}, {self.y1}, {self.x2}, {self.y2})"

    def getXY(self):
        return self.x1, self.y1, self.x2, self.y2

    def isHorizontal(self):
        return self.x1 != self.x2

    def isVertical(self):
        return self.y1 != self.y2

    def draw(self, board):
        print(
            f"Move: {self.x1, self.y1, self.x2, self.y2} Rating: {self.rate(board)}")

    def rate(self, board):
        """Counts the number of boxes that this move completes right now"""
        rating = 0
        row, col = board.getCell(self.x1, self.y1, self.x2, self.y2)
        g = board.grid
        if self.isHorizontal():
            # two possible boxes can be filled - an above, and a below
            # above
            if self.y1 != 0:
                edges = [
                    g[row-1][col-1],
                    g[row-1][col+1],
                    g[row-2][col],
                ]
                if edges.count(" ") % 2 == 0:
                    rating += 3-edges.count(" ")
            # below
            if self.y1 != board.height:
                edges = [
                    g[row+1][col-1],
                    g[row+1][col+1],
                    g[row+2][col],
                ]
                if edges.count(" ") % 2 == 0:
                    rating += 3-edges.count(" ")
        if self.isVertical():
            # two possible boxes can be filled - an left and a right

            # left
            if self.x1 != 0:
                edges = [
                    g[row-1][col-1],
                    g[row+1][col-1],
                    g[row][col-2],
                ]
                if edges.count(" ") % 2 == 0:
                    rating += 3-edges.count(" ")
            # right
            if self.x1 != board.width:
                edges = [
                    g[row-1][col+1],
                    g[row+1][col+1],
                    g[row][col+2],
                ]
                if edges.count(" ") % 2 == 0:
                    rating += 3-edges.count(" ")
        if rating > 4:
            raise Exception("Rating Condition Error")
        return rating
