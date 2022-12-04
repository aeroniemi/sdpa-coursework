class Board ():
    def __init__(self, width, height):
        """
        @width: int, number of boxes in X axis
        @height: int, number of boxes in Y axis
        """
        if not (type(width) is int and type(height) is int):
            raise TypeError("Board dimensions should be int")
        if width < 2 or height < 2:
            raise Exception("Board size must be greater than 3x3")
        self.width = width
        self.height = height
        self.build()

    def build(self):
        self.hLines = []
        self.vLines = []
        for i in range(1, self.width):
            self.hLines.append([None]*self.height)
        for i in range(1, self.height):
            self.vLines.append([None]*self.width)

    def draw(self):
        print("Drawing Board")
        for i in range(self.height, 0, -1):
            print("•-" * self.width + "•")
            print("| " * self.width + "|")
        print("•-" * self.width + "•")
