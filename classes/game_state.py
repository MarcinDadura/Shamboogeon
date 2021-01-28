class GameState:
    '''
    Provide simple access to current level, room coordinates...
    '''
    _instance = None

    def __init__(self):
        self.current_lvl = 0
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