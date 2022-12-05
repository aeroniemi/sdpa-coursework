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
        for i in range(self.height, -1, -1):
            print(i)
            strh = ""
            for j in range(self.width):
                strh += f"•{self.hLines[j][i] or ' '}"
            strh += "•"
            print(strh)
            strv = ""
            if i == 0:
                break
            for j in range(self.width):
                strv += f"{self.vLines[j][i-1] or ' '} "
            print(strv)
        #     print("•-" * self.width + "•")
        #     print("| " * self.width + "|")
        # print("•-" * self.width + "•")

    def validateCoord(self, coord):
        x, y = coord
        if x >= 0 and x <= self.width and y >= 0 and y <= self.width:
            return True
        return False

    def addLine(self, c1, c2, player):
        if not self.validateCoord(c1):
            raise Exception("Coordinate 1 is out of range")
        if not self.validateCoord(c2):
            raise Exception("Coordinate 2 is out of range")

        x1, y1 = c1
        x2, y2 = c2
        if x1 == x2:
            self.addVerticalLine(c1,  player)
        if y1 == y2:
            self.addHorizontalLine(c1,  player)

        self.draw()

    def addVerticalLine(self, c1, player):
        x = c1[0]
        self.vLines[c1[0]][c1[1]] = player
