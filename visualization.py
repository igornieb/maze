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
    pygame.display.set_caption("maze")
    surface = pygame.display.set_mode(RES)
    clock = pygame.time.Clock()

    m = Maze()
    m.random_maze(X, Y)

    start = m.start
    end = m.end
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

    a_path, fwd_path = m.get_path_a_star()
    for current in a_path:
        handle_events()
        if current != start:
            pygame.draw.rect(surface, pygame.Color("darkgray"),
                         (current[0] * TILE + 2, current[1] * TILE + 2, TILE - 2, TILE - 2))
        pygame.display.flip()
        clock.tick(FPS)

    for block in fwd_path:
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
    while True:
        handle_events()
        clock.tick(FPS)


if __name__ == '__main__':
    visualize_path_finding()
