from typing import *
from Block import Block
import random
from queue import PriorityQueue
from mazegenerator import maze_gen

class Maze:
    maze = list()

    def readFromFile(self, infile):
        try:
            file = open(infile, "r")
            for line in file:
                mazeLine = list()
                line = line.replace("\n", "")
                for char in line:
                    mazeLine.append(Block(char))
                self.maze.append(mazeLine)
            file.close()
            return self.maze
        except:
            exit()

    def generateMaze(self, x, y):
        tmp=maze_gen(x,y)
        for i in range(x):
            line=list()
            for j in range(y):
                line.append(Block(tmp[i][j]))
            self.maze.append(line)

    def randomMaze1(self, x, y):
        for i in range(x):
            line=list()
            for j in range(y):
                line.append(Block("#"))
            self.maze.append(line)
        for i in range(x):
            for j in range(y):
                n = self.getTopOrLeft([i,j])
                if n is not None:
                    n.setSymbol(" ")

        rx = random.randint(1,x-1)
        ry = random.randint(1,x-1)
        start = self.maze[0][rx]
        start.setSymbol("s")
        end = self.maze[y-1][ry]
        end.setSymbol("e")
    def getTopOrLeft(self, index):
        x = index[0]
        y = index[1]
        blocks = list()
        if x - 1 >= 0:
            blocks.append(self.maze[x - 1][y])
        if y - 1 >= 0:
            blocks.append(self.maze[x][y - 1])
        if len(blocks) > 0:
            return random.choice(blocks)
        else:
            return None

    def printMaze(self) -> None:
        for line in self.maze:
            m = str()
            for block in line:
                m += str(block.getSymbol())
            print(m)

    def endIndex(self) -> tuple:
        for i in range(0, len(self.maze)):
            for j in range(0, len(self.maze[i])):
                if self.maze[i][j].getSymbol() == 'e':
                    self.maze[i][j].setValue(0)
                    return (i, j)

    def startIndex(self) -> tuple:
        for i in range(0, len(self.maze)):
            for j in range(0, len(self.maze[i])):
                if self.maze[i][j].getSymbol() == 's':
                    return (i, j)

    def findIndexesWithValue(self, value) -> List[Block]:
        indexes = list()
        for i in range(0, len(self.maze)):
            for j in range(0, len(self.maze[i])):
                if self.maze[i][j].getValue() == value:
                    indexes.append(self.maze[i][j])
        return indexes

    def blocksToSet(self) -> bool:
        # returns trueif there are still blocks whith unasined values in maze instance
        for i in range(0, len(self.maze)):
            for j in range(0, len(self.maze[i])):
                if self.maze[i][j].isWalkable() is True and self.maze[i][j].isSet() is False:
                    return True

    def findNearby(self, index) -> List[Block]:
        # find left right top bottom, neighbours of blokck, return only blocks that arent not set
        x = len(self.maze) - 1
        y = len(self.maze[0]) - 1
        nearbyBlocks = list()
        # find left
        if index[0] > 0:
            tmpBlock = self.maze[index[0] - 1][index[1]]
            if tmpBlock.isWalkable():
                nearbyBlocks.append(tmpBlock)
        # right
        if index[0] < x:
            tmpBlock = self.maze[index[0] + 1][index[1]]
            if tmpBlock.isWalkable():
                nearbyBlocks.append(tmpBlock)
        # top
        if index[1] > 0:
            tmpBlock = self.maze[index[0]][index[1] - 1]
            if tmpBlock.isWalkable():
                nearbyBlocks.append(tmpBlock)
        # bottom
        if index[1] < y:
            tmpBlock = self.maze[index[0]][index[1] + 1]
            if tmpBlock.isWalkable():
                nearbyBlocks.append(tmpBlock)
        return nearbyBlocks

    def findBlockIndex(self, block) -> tuple:
        for i in range(0, len(self.maze)):
            for j in range(0, len(self.maze[i])):
                if self.maze[i][j] == block:
                    return (i, j)

    def assignBlockValues(self) -> None:
        #used for solving with BFS
        self.endIndex()
        value = 0
        while self.blocksToSet():
            IndexesWithValue = self.findIndexesWithValue(value)
            value += 1
            for indexWithValue in IndexesWithValue:
                index = self.findBlockIndex(indexWithValue)
                tmpBlocks = self.findNearby(index)
                for block in tmpBlocks:
                    block.setValue(value)

    def listAllElements(self) -> List[Block]:
        tab = list()
        for i in range(0, len(self.maze)):
            for j in range(0, len(self.maze[i])):
                if self.maze[i][j].isWalkable():
                    tab.append(self.maze[i][j])
        return tab

    def solveMazeBFS(self) -> None:
        # asign values based on distance from end
        self.assignBlockValues()
        # path finding using BFS algorithm
        start = self.maze[self.endIndex()[0]][self.endIndex()[1]]
        end = self.maze[self.startIndex()[0]][self.startIndex()[1]]
        frontier = [start]
        explored = [start]
        path = {}
        # traversing through all possible ways
        while len(frontier) > 0:
            currentBlock = frontier.pop(0)
            if currentBlock == end:
                break
            n = self.findNearby(self.findBlockIndex(currentBlock))
            for u in n:
                if u in explored:
                    continue
                frontier.append(u)
                explored.append(u)
                path[u] = currentBlock
        self.endIndex()
        fwdPath = {}
        block = end
        # swap keys with values
        while block != start:
            fwdPath[path[block]] = block
            block = path[block]

        # swap symbols in path to *
        for block in fwdPath:
            if block.getSymbol() != "e":
                block.symbol = "*"

    def h(self, cell1, cell2):
        # returns distance from cell1 to cell2 (current cell) to (end cell)
        x1, y1 = cell1
        x2, y2 = cell2
        return abs(x1 - x2) + abs(y1 + y2)

    def solveMazeAstar(self):
        aPath = {}
        start = self.endIndex()
        end = self.startIndex()
        g_value = {}
        f_value = {}
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                g_value[(i,j)]=float("inf")
                f_value[(i,j)]=float("inf")
        g_value[start] = 0
        g_value[start] = self.h(start, end)
        queue = PriorityQueue()
        queue.put((self.h(start, end), self.h(start, end), start))

        while not queue.empty():
            current = queue.get()[2]
            if current == end:
                break
            else:
                n = self.findNearby(current)
                for block in n:
                    block = self.findBlockIndex(block)
                    tmp_g_value = g_value[current] + 1
                    tmp_f_value = tmp_g_value + self.h(block, end)
                    if tmp_f_value < f_value[block]:
                        g_value[block] = tmp_g_value
                        f_value[block] = tmp_f_value
                        queue.put((tmp_f_value, self.h(block, end), block))
                        aPath[block] = current
        fwdPath = {}
        block = end
        # swap keys with values
        while block != start:
            fwdPath[aPath[block]] = block
            block = aPath[block]

        for block in fwdPath:
            cell = self.maze[block[0]][block[1]]
            if cell.getSymbol() != "e":
                cell.symbol = "*"