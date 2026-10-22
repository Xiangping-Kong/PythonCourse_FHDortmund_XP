from checker import Checker  # 导入 Checker 类

class Board:
    """ Board 类：管理 8x8 棋盘数组与可视化打印 """
    def __init__(self, board_type=1):
        self.board_type = board_type
        self.size = 8
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.setup_board()

    def setup_board(self):
        """ 初始化棋盘（支持两种不同配置） """
        if self.board_type == 1:
            # 类型 1：标准摆法（前3行黑棋，后3行红棋）
            for r in range(3):
                for c in range(8):
                    if (r + c) % 2 == 1:
                        self.grid[r][c] = Checker('B', r, c)
            for r in range(5, 8):
                for c in range(8):
                    if (r + c) % 2 == 1:
                        self.grid[r][c] = Checker('R', r, c)
        else:
            # 类型 2：简易测试模式（少放几个棋子）
            self.grid[2][1] = Checker('B', 2, 1)
            self.grid[5][2] = Checker('R', 5, 2)

    def display(self):
        """ 打印棋盘状态 """
        print("\n" + "=" * 35)
        print("         当前棋盘状态 (Board)")
        print("=" * 35)
        print("     0   1   2   3   4   5   6   7")
        print("   +" + "---+" * 8)
        
        for r in range(self.size):
            row_str = f" {r} |"
            for c in range(self.size):
                checker = self.grid[r][c]
                if checker:
                    row_str += f" {checker} |"
                else:
                    cell = " . " if (r + c) % 2 == 1 else "   "
                    row_str += f"{cell}|"
            print(row_str)
            print("   +" + "---+" * 8)
        print("图例: [r]=红棋 | [b]=黑棋")

    def move_checker(self, start_r, start_c, end_r, end_c):
        """ 极简移动逻辑：直接转移棋子对象 """
        checker = self.grid[start_r][start_c]
        self.grid[start_r][start_c] = None
        self.grid[end_r][end_c] = checker
        checker.row, checker.col = end_r, end_c