class Gamestats:
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ships_left = None
        self.ai_settings = ai_settings
        self.reset_stats()

        # 刚启动时处于激活状态
        self.game_active = False

    def reset_stats(self):
        """初始化游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
