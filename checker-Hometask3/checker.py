class Checker:
    """ Checker 类：表示单个棋子 """
    def __init__(self, color, row, col):
        self.color = color  # 'R' (红方) 或 'B' (黑方)
        self.row = row
        self.col = col

    def __str__(self):
        # 控制台显示的符号：r 代表红棋，b 代表黑棋
        return self.color.lower()