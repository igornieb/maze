from Maze import Maze


def test():
    m = Maze()
    # reads maze from given file
    m.read_from_file("maze.txt")

    # (DFS) Depth First Traversal maze generation
    #m.random_maze(10, 20)

    # A* algorithm solver
    m.solve_maze_a_star()
    m.print_maze()


def help():
    print("""
    *Info
        This python script solves mazes - finds and marks shortest path 
        from start to end of a maze using A* (A star) algorithm.
        In main.py you can find function test() which contains other methods 
        of finding shortest path in a maze.
    *Solving from file
        File should contain:
        \t# - walls
        \t - passgaes (whitespaces)
        \te - exit (only one)
        \ts - start (only one)
        Example text file:
        #e#####
        # #   #
        #     #
        #  #  #
        # ### #
        #  #  #
        #     #
        #   # #
        #####s#
    
    ###########[MAZE SOLVER]###########
    #######[IGOR NIEBYLSKI 2022]#######
    """)


def menu():
    print("""
    ###########[MAZE SOLVER]###########
    1. Solve maze loaded from from file 
    2. Solve randomly generated maze
    3. Help
    4. Exit
    #######[IGOR NIEBYLSKI 2023]#######
    """)


def maze():
    menu()
    ans = int(input("Chose option from 1 to 4: "))
    m = Maze()
    if ans == 1:
        infile = input("\tSpecify file directory: ")
        m.read_from_file(infile)
    if ans == 2:
        y = int(input("\tMaze width: "))
        x = int(input("\tMaze height: "))
        m.random_maze_2(x, y)
    if ans == 3:
        help()
        exit()
    if ans == 4:
        exit()

    m.solve_maze_a_star()
    m.print_maze()
    input("Press Enter to continue.")


if __name__ == '__main__':
    test()
