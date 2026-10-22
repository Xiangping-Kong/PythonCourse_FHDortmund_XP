import time  
from player import Player  # 导入 Player 类[cite: 11]
from board import Board    # 导入 Board 类[cite: 11]

class Game:
    """ Game 类：管理游戏整体流程、计时与总结 """
    def __init__(self):
        print("=== Python 跳棋游戏 (简易 OOP 版) ===")
        p1 = input("请输入玩家 1 (红方) 姓名 [默认 Player1]: ").strip() or "Player1"
        p2 = input("请输入玩家 2 (黑方) 姓名 [默认 Player2]: ").strip() or "Player2"
        
        b_choice = input("请选择棋盘类型 (1: 标准, 2: 残局测试) [默认 1]: ").strip()
        board_type = 2 if b_choice == '2' else 1

        self.player1 = Player(p1, 'R')
        self.player2 = Player(p2, 'B')
        self.board = Board(board_type)
        self.current_player = self.player1
        self.start_time = None

    def start(self):
        self.start_time = time.time()
        
        while True:
            # 1. 显示棋盘和当前玩家状态[cite: 12]
            self.board.display()
            print(f"\n>>>> {self.current_player.get_info()} <<<<")
            
            # 2. 移动前询问：移动 还是 结束游戏[cite: 12]
            print("\n请选择操作:")
            print(" [1] 移动棋子 (Move)")
            print(" [2] 结束游戏 (Finish Game)")
            choice = input("请输入选项 (1 或 2): ").strip()

            if choice == '2':
                # 选择主动结束游戏[cite: 12]
                print(f"\n玩家 {self.current_player.name} 选择主动结束游戏！")
                self.current_player.result = "主动退出"
                other = self.player2 if self.current_player == self.player1 else self.player1
                other.result = "获胜"
                break
                
            elif choice == '1':
                try:
                    coords = input("请输入移动坐标 (格式: 起始行 起始列 目标行 目标列，例如 5 0 4 1): ").split()
                    if len(coords) != 4:
                        print("❌ 格式错误！请输入 4 个用空格隔开的数字。")
                        continue
                        
                    sr, sc, er, ec = map(int, coords)
                    
                    # 简化后的合法性校验
                    checker = self.board.grid[sr][sc]
                    if not checker:
                        print("❌ 起始位置没有棋子！")
                        continue
                    if checker.color != self.current_player.color:
                        print("❌ 不能移动对方的棋子！")
                        continue
                    if self.board.grid[er][ec] is not None:
                        print("❌ 简化规则：目标位置已有棋子，不能覆盖！")
                        continue

                    # 执行移动
                    self.board.move_checker(sr, sc, er, ec)
                    self.current_player.moves_count += 1
                    
                    # 轮换玩家
                    self.current_player = self.player2 if self.current_player == self.player1 else self.player1

                except ValueError:
                    print("❌ 输入无效！请输入有效的数字坐标。")
            else:
                print("❌ 选项无效，请输入 1 或 2。")

        # 3. 游戏结束后显示总结[cite: 12]
        self.show_summary()

    def show_summary(self):
        total_time = round(time.time() - self.start_time, 2)
        print("\n==========================================")
        print("           游戏总结 (Game Summary)        ")
        print("==========================================")
        print(f"游戏总用时: {total_time} 秒")
        print("-" * 42)
        print(f"玩家 1 [{self.player1.name}]:")
        print(f"  - 棋子颜色: 红方 (R)")
        print(f"  - 移动步数: {self.player1.moves_count}")
        print(f"  - 最终结果: {self.player1.result}")
        print("-" * 42)
        print(f"玩家 2 [{self.player2.name}]:")
        print(f"  - 棋子颜色: 黑方 (B)")
        print(f"  - 移动步数: {self.player2.moves_count}")
        print(f"  - 最终结果: {self.player2.result}")
        print("==========================================")

# 程序入口
if __name__ == "__main__":
    game = Game()
    game.start()