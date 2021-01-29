class GameState:
    '''
    Provide simple access to current level, room coordinates...
    '''
    _instance = None

    def __init__(self):
        self.current_lvl = 0
        self.board_scale = 1
        self.exit = False
        self.next_lvl = False
        GameState._instance = self

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            # Create instance
            cls()
        return cls._instance

    def get_current_lvl(self) -> int:
        return self.current_lvl

    def set_current_lvl(self, lvl: int):
        self.current_lvl = lvl

    def set_board_scale(self, scale: int):
        self.board_scale = scale

    def get_board_scale(self) -> int:
        return self.board_scale

    def reset(self):
        """Reset all values"""
        self.current_lvl = 0
        self.board_scale = 1
