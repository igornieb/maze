import pygame
from Maze import Maze
from queue import PriorityQueue

# screen resolution
RES = HEIGHT, WIDTH = 900, 900
# tile size
TILE = 30
# speed
FPS = 60

PASSAGE = " "
WALL = "#"

X = int(HEIGHT / TILE)
Y = int(WIDTH / TILE)


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


def visualize_path_finding():
    pygame.init()
    surface = pygame.display.set_mode(RES)
    clock = pygame.time.Clock()

    m = Maze()
    m.random_maze(X, Y)

    a_path = {}
    start = m.start
    end = m.end
    walkable_elements = m.list_all_walkable_elements()
    g_value = {(block.x, block.y): float('inf') for block in walkable_elements}
    g_value[start] = 0
    f_value = {(block.x, block.y): float('inf') for block in walkable_elements}
    g_value[start] = m.h(start, end)
    queue = PriorityQueue()
    queue.put((m.h(start, end), m.h(start, end), start))

    surface.fill(pygame.Color('black'))
    # draw maze
    [pygame.draw.line(surface, pygame.Color('dimgray'), (x, 0), (x, HEIGHT)) for x in range(0, WIDTH, TILE)]
    [pygame.draw.line(surface, pygame.Color('dimgray'), (0, y), (WIDTH, y)) for y in range(0, HEIGHT, TILE)]

    for x in range(0, X):
        for y in range(0, Y):
            if m.maze[x][y].get_symbol() == WALL:
                pygame.draw.rect(surface, pygame.Color("white"), (x * TILE + 2, y * TILE + 2, TILE - 2, TILE - 2))
            if m.maze[x][y].get_symbol() == "s" or m.maze[x][y].get_symbol() == "e":
                pygame.draw.rect(surface, pygame.Color("yellow"), (x * TILE + 2, y * TILE + 2, TILE - 2, TILE - 2))

    # begin pathfinding
    while True:
        while not queue.empty():
            handle_events()
            #
            current = queue.get()[2]
            if current == end:
                queue = PriorityQueue()
                break
            else:
                n = m.find_nearby(current)
                for block in n:
                    block = (block.x, block.y)
                    tmp_g_value = g_value[current] + 1
                    tmp_f_value = tmp_g_value + m.h(block, end)
                    if tmp_f_value < f_value[block]:
                        g_value[block] = tmp_g_value
                        f_value[block] = tmp_f_value
                        queue.put((tmp_f_value, m.h(block, end), block))
                        a_path[block] = current

                        # draw current block on screen as visited
                        if current != start:
                            pygame.draw.rect(surface, pygame.Color("darkgray"),
                                             (current[0] * TILE + 2, current[1] * TILE + 2, TILE - 2, TILE - 2))

            pygame.display.flip()
            clock.tick(FPS)

        fwdPath = {}
        block = end
        # swap keys with values
        while block != start:
            handle_events()
            #
            fwdPath[a_path[block]] = block
            block = a_path[block]

        for block in fwdPath:
            handle_events()
            #
            cell = m.maze[block[0]][block[1]]
            if cell.get_symbol() != "e":
                pygame.draw.rect(surface, pygame.Color("yellow"),
                                 (cell.x * TILE + 2, cell.y * TILE + 2, TILE - 2, TILE - 2))
                pygame.display.flip()
                clock.tick(FPS)

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    visualize_path_finding()
