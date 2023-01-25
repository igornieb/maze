class Block:
    symbol = None
    walkable = False  # is it a wall or is it a route
    value = None  # how far is it from end - used for finding path alghoritm - BFS
    x=None
    y=None
    def __init__(self, symbol):
        self.symbol = symbol
        if symbol == "#":
            self.walkable = False
        else:
            self.walkable = True

    def getSymbol(self) -> str:
        return self.symbol

    def setSymbol(self, symbol) -> None:
        if symbol == "#":
            self.walkable=False
        else:
            self.walkable = True
            self.symbol = symbol

    def isWalkable(self) -> bool:
        if self.walkable is True:
            return True
        return False

    def isSet(self) -> bool:
        if self.value is None:
            return False
        return True

    def setValue(self, value) -> None:
        if self.isSet() is False:
            self.value = value

    def getValue(self):
        return self.value