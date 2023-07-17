from Maze import Maze
from visualization import visualize_path_finding


def test():
    m = Maze()
    # reads maze from given file
    m.read_from_file("maze.txt")

    # Depth First Traversal maze generation
    m.random_maze(20, 20)

    # A* algorithm implementation
    m.solve_maze_a_star()
    m.print_maze()

    # combines dfs generation, a* and visualizes path finding
    visualize_path_finding()


if __name__ == '__main__':
    visualize_path_finding()
