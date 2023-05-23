from typing import *
from Block import Block
import random
from queue import PriorityQueue
from mazegenerator import random_maze_generator


class Maze:
    maze = list()
    start = (0, 0)
    end = (0, 0)

    def read_from_file(self, infile):
        try:
            file = open(infile, "r")
            x = 0
            for line in file:
                mazeLine = list()
                line = line.replace("\n", "")
                y = 0
                for char in line:
                    mazeLine.append(Block(char, x, y))
                    if char == "e":
                        self.end = (x, y)
                    if char == "s":
                        self.start = (x, y)
                    y += 1
                self.maze.append(mazeLine)
                x += 1
            file.close()
            return self.maze
        except:
            exit()

    def random_maze(self, x, y):
        rx = random.randint(0, y - 1)
        start = [0, rx]
        ry = random.randint(0, y - 1)
        end = [x - 1, ry]
        randomMaze = random_maze_generator(x, y, start, end)
        for i in range(x):
            line = list()
            # line.append(Block("#"))
            for j in range(y):
                if randomMaze[i][j] == 0:
                    line.append(Block("#", i, j))
                if randomMaze[i][j] == 1:
                    line.append(Block(" ", i, j))
                if randomMaze[i][j] == 2:
                    line.append(Block("s", i, j))
                    self.start = (i, j)
                if randomMaze[i][j] == 3:
                    line.append(Block("e", i, j))
                    self.end = (i, j)
            self.maze.append(line)

    def print_maze(self) -> None:
        for line in self.maze:
            m = str()
            for block in line:
                m += str(block.get_symbol())
            print(m)

    def find_indexes_with_value(self, value) -> List[Block]:
        indexes = list()
        for i in range(0, len(self.maze)):
            for j in range(0, len(self.maze[i])):
                if self.maze[i][j].get_value() == value:
                    indexes.append(self.maze[i][j])
        return indexes

    def blocks_to_set(self) -> bool:
        for i in range(0, len(self.maze)):
            for j in range(0, len(self.maze[i])):
                if self.maze[i][j].is_walkable() is True and self.maze[i][j].is_set() is False:
                    return True

    def find_nearby(self, index) -> List[Block]:
        # find left right top bottom, return only blocks that arent not set
        x = len(self.maze) - 1
        y = len(self.maze[0]) - 1
        nearbyBlocks = list()
        # find left
        if index[0] > 0:
            tmpBlock = self.maze[index[0] - 1][index[1]]
            if tmpBlock.is_walkable():
                nearbyBlocks.append(tmpBlock)
        # right
        if index[0] < x:
            tmpBlock = self.maze[index[0] + 1][index[1]]
            if tmpBlock.is_walkable():
                nearbyBlocks.append(tmpBlock)
        # top
        if index[1] > 0:
            tmpBlock = self.maze[index[0]][index[1] - 1]
            if tmpBlock.is_walkable():
                nearbyBlocks.append(tmpBlock)
        # bottom
        if index[1] < y:
            tmpBlock = self.maze[index[0]][index[1] + 1]
            if tmpBlock.is_walkable():
                nearbyBlocks.append(tmpBlock)
        return nearbyBlocks

    def list_all_walkable_elements(self) -> List[Block]:
        tab = list()
        for i in range(0, len(self.maze)):
            for j in range(0, len(self.maze[i])):
                if self.maze[i][j].is_walkable():
                    tab.append(self.maze[i][j])
        return tab
    def h(self, cell1, cell2):
        # returns distance from cell1 to cell2 (current cell) to (end cell)
        x1, y1 = cell1
        x2, y2 = cell2
        return abs(x1 - x2) + abs(y1 + y2)

    def solve_maze_a_star(self) -> None:
        aPath = {}
        start = self.start
        end = self.end
        walkable_elements = self.list_all_walkable_elements()
        g_value = {(block.x, block.y): float('inf') for block in walkable_elements}
        g_value[start] = 0
        f_value = {(block.x, block.y): float('inf') for block in walkable_elements}
        g_value[start] = self.h(start, end)
        queue = PriorityQueue()
        queue.put((self.h(start, end), self.h(start, end), start))

        while not queue.empty():
            current = queue.get()[2]
            if current == end:
                break
            else:
                n = self.find_nearby(current)
                for block in n:
                    block = (block.x, block.y)
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
            if cell.get_symbol() != "e":
                cell.symbol = "*"
