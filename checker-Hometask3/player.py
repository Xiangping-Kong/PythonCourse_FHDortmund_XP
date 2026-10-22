class Player:
    """ Player 类：存储玩家信息与统计数据 """
    def __init__(self, name, color):
        self.name = name
        self.color = color      # 'R' 或 'B'
        self.moves_count = 0    # 移动步数统计
        self.result = "进行中"   # 游戏结果

    def get_info(self):
        color_str = "红方 (r)" if self.color == 'R' else "黑方 (b)"
        return f"玩家: {self.name} | 执棋: {color_str} | 已走步数: {self.moves_count}"