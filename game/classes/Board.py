class Board ():
    def __init__(self, width, height):
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
                        row[j] = "•"

    def draw(self):
        print("Drawing Board")
        print(" "+" ".join(str(i) for i in range(0, self.width+1)))
        for i in range(len(self.grid)):
            s = ""
            if i % 2 == 0:
                s += str(i // 2)
            else:
                s += " "
            for cell in self.grid[i]:
                s += cell or " "
            print(s)

    def validateMove(self, x1, y1, x2, y2):
        return True

    def addLine(self, x1, y1, x2, y2, player):
        isValid = self.validateMove(x1, y1, x2, y2)
        if not isValid:
            raise Exception("Not a valid move")
        self.setLine(x1, y1, x2, y2, player)

    def setLine(self, x1, y1, x2, y2, player):
        row = y1*2 if y1 == y2 else min(y1, y2)*2+1
        col = x1*2 if x1 == x2 else min(x1, x2)*2+1
        self.grid[row][col] = "@"
        return True


# 0, 1 - 1
# 1, 2 - 3
# 2, 3 - 5
