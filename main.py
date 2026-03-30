import random

class Grid:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return self.__str__()

class Line:
    """判定ラインの管理"""
    def __init__(self, grids: list[Grid], is_reach: bool = False, is_bingo: bool = False):
        self.grids = grids
        self.is_reach = is_reach
        self.is_bingo = is_bingo

class Cell:
    """マスの番号やマーク状態の管理"""
    def __init__(self, number: int, is_hit: bool = False):
        self.number = number
        self.is_hit = is_hit

    def __str__(self):
        if self.number == 0:
            return "FREE"
        else:
            if self.is_hit:
                return f"({self.number:02})"
            else:
                return f" {self.number:02} "

    def __repr__(self):
        return self.__str__()

class Bingo:
    def __init__(self, size: int):
        self.size = size

        self.lines: list[Line] = []
        """判定用ライン"""
        self.card: list[list[Cell]] = []
        """ビンゴカード"""
        self.cell_dict: dict[int, Grid] = {}
        """カード逆引き"""
        self.number_pool: list[int] = [i for i in range(1, size * 15 + 1)]
        self.history: list[int] = []

        self.bingo: int = 0
        self.reach: int = 0

        self.init_lines()
        self.init_card()

    def init_lines(self):
        """判定用ラインの初期化"""
        self.lines = []
        for line_x in range(0, self.size): # 縦ライン
            new_line: list[Grid] = []
            for line_y in range(0, self.size):
                new_line.append(Grid(line_x, line_y))
            self.lines.append(Line(new_line.copy()))

        for line_y in range(0, self.size): # 横ライン
            new_line: list[Grid] = []
            for line_x in range(0, self.size):
                new_line.append(Grid(line_x, line_y))
            self.lines.append(Line(new_line.copy()))

        line_lt_rb: list[Grid] = [] # Left top -> Right bottom
        line_lb_rt: list[Grid] = [] # Left bottom -> Right top
        for i in range(0, self.size): # クロスライン
            line_lt_rb.append(Grid(i, i))
            line_lb_rt.append(Grid(i, self.size - 1 - i))
        self.lines.append(Line(line_lt_rb.copy()))
        self.lines.append(Line(line_lb_rt.copy()))

    def init_card(self):
        """ビンゴカードの初期化"""
        self.card = []
        for _ in range(self.size):
            self.card.append([])

        for line_x in range(0, self.size):
            numbers = random.sample(range(line_x*15 + 1, line_x*15 + 16), k=self.size)
            for line_y in range(0, self.size):
                self.card[line_x].append(Cell(numbers[line_y]))
                self.cell_dict[numbers[line_y]] = Grid(line_x, line_y)

        # Free
        center = self.size // 2
        self.cell_dict.pop(self.card[center][center].number)
        self.card[center][center].number, self.card[center][center].is_hit = 0, True

    def print_card(self):
        """ビンゴカードの表示"""
        for y in range(0, self.size):
            for x in range(self.size):
                print(self.card[x][y], end="")
            print()

    def draw(self) -> int:
        drew = self.number_pool.pop(random.randrange(0, len(self.number_pool)))
        self.history.append(drew)
        return drew

    def update_card(self, number: int):
        grid = self.cell_dict.get(number)
        if grid:
            self.card[grid.x][grid.y].is_hit = True

    def update_lines(self):
        for i in range(len(self.lines)):
            line = self.lines[i]
            if line.is_bingo:
                continue
            hits = 0
            for grid in line.grids:
                if self.card[grid.x][grid.y].is_hit:
                    hits += 1
            if hits == self.size:
                self.lines[i].is_bingo = True
                self.bingo += 1
                self.reach -= 1
            elif hits == (self.size - 1) and not self.lines[i].is_reach:
                self.lines[i].is_reach = True
                self.reach += 1

    def play_turn(self) -> int:
        """ビンゴゲームの進行"""
        drew = self.draw()
        self.update_card(drew)
        self.update_lines()
        return drew

def main():
    bingo = Bingo(5)
    while bingo.number_pool:
        drew = bingo.play_turn()
        print(f"Ball[{len(bingo.history)}] = {drew}")
        print()
        bingo.print_card()
        print()
        print(f"REACH = {bingo.reach}")
        print(f"BINGO = {bingo.bingo}")
        print("-"*20)

if __name__ == "__main__":
    main()
