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
        """判定用ライン"""
        self.card: list[list[int]] = []
        """ビンゴカード"""
        self.init_lines()
        self.init_card()

    def init_lines(self):
        """判定用ラインの初期化"""
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

    def init_card(self):
        """ビンゴカードの初期化"""
        pass

    def print(self):
        """ビンゴの状態の表示"""
        pass

    def run(self):
        """ビンゴゲームの進行"""
        pass

def main():
    bingo = Bingo()

if __name__ == "__main__":
    main()
