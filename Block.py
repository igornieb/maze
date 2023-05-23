class Block:
    symbol = None
    walkable = False  # is it a wall or is it a route
    value = None  # how far is it from end - used for first path algorithm - BFS

    def __init__(self, symbol, x, y):
        self.symbol = symbol
        if symbol == "#":
            self.walkable = False
        else:
            self.walkable = True
        self.x = x
        self.y = y

    def get_symbol(self) -> str:
        return self.symbol

    def set_symbol(self, symbol) -> None:
        if symbol == "#":
            self.walkable=False
        else:
            self.walkable = True
            self.symbol = symbol

    def is_walkable(self) -> bool:
        if self.walkable is True:
            return True
        return False

    def is_set(self) -> bool:
        if self.value is None:
            return False
        return True

    def set_value(self, value) -> None:
        if self.is_set() is False:
            self.value = value

    def get_value(self):
        return self.value