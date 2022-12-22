class Move:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self):
        return f"({self.x1}, {self.y1}, {self.x2}, {self.y2})"

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
        if self.isHorizontal():
            # two possible boxes can be filled - an above, and a below
            # above
            if self.y1 != 0:
                edges = [
                    (self.x1, self.y1, self.x1, self.y1-1),
                    (self.x1, self.y1-1, self.x1+1, self.y1-1),
                    (self.x1+1, self.y1-1, self.x1+1, self.y1-1)
                ]
                if edges[0] != " " and len(set(edges)) == 1:
                    rating += 1
            # below
            if self.y1 != len(board.grid):
                edges = [
                    (self.x1, self.y1, self.x1, self.y1+11),
                    (self.x1, self.y1+1, self.x1+1, self.y1+1),
                    (self.x1+1, self.y1+1, self.x1+1, self.y1+1)
                ]
                if edges[0] != " " and len(set(edges)) == 1:
                    rating += 1
        if self.isVertical():
            # two possible boxes can be filled - an left and a right

            # left
            if self.y1 != 0:
                edges = [
                    (self.x1-1, self.y1, self.x1, self.y1),
                    (self.x1-1, self.y1, self.x1-1, self.y1+1),
                    (self.x1-1, self.y1+1, self.x1, self.y1+1)
                ]
                if edges[0] != " " and len(set(edges)) == 1:
                    rating += 1
            # right
            if self.y1 != len(board.grid):
                edges = [
                    (self.x1, self.y1, self.x1+1, self.y1),
                    (self.x1+1, self.y1, self.x1+1, self.y1+1),
                    (self.x1, self.y1+1, self.x1+1, self.y1+1)
                ]
                if edges[0] != " " and len(set(edges)) == 1:
                    rating += 1

        if rating > 2:
            raise Exception("Rating Condition Error")
        return rating
