import random

class Grid:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return self.__str__()

class Bingo:
    def __init__(self):
        self.lines: list[list[Grid]] = []
        self.init_lines()

    def init_lines(self):
        for line_x in range(0, 5): # 縦ライン
            new_line: list[Grid] = []
            for line_y in range(0, 5):
                new_line.append(Grid(line_x, line_y))
            self.lines.append(new_line.copy())

        for line_y in range(0, 5): # 横ライン
            new_line: list[Grid] = []
            for line_x in range(0, 5):
                new_line.append(Grid(line_x, line_y))
            self.lines.append(new_line.copy())

        line_lt_rb: list[Grid] = [] # Left top -> Right bottom
        line_lb_rt: list[Grid] = [] # Left bottom -> Right top
        for i in range(0, 5): # クロスライン
            line_lt_rb.append(Grid(i, i))
            line_lb_rt.append(Grid(i, 4 - i))
        self.lines.append(line_lt_rb.copy())
        self.lines.append(line_lb_rt.copy())

def main():
    bingo = Bingo()

if __name__ == "__main__":
    main()
