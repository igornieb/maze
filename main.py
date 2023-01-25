from Maze import Maze

def test():
    m = Maze()
    # reads maze from given file
    # m.readFromFile("maze.txt")

    # (DFS) Depth First Traversal maze generation
    m.randomMaze2(9, 7)
    # binary tree maze generation
    # m.randomMaze1(10,10)

    # BFS maze solver fine for smaller mazes
    # m.solveMazeBFS()
    # A* algorithm solver
    m.solveMazeAstar()
    m.printMaze()

def help():
    print("""
    *Info
        This python script solves mazes - finds and marks shortest path 
        from start to end of a maze using A* (A star) algorithm.
        In main.py you can find function test() which contains other methods 
        of finding shortest path in a maze.
        I tested it for mazes up to size of 150x150. For mazes bigger than 100x100
        it takes considerable amount of time to execute.
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
        ans = int(input("Chose option from 1 to 3: "))
        m = Maze()
        if ans == 1:
            infile = input("\tSpecify file directory: ")
            m.readFromFile(infile)
        if ans == 2:
            y = int(input("\tMaze width: "))
            x = int(input("\tMaze height: "))
            m.generateMaze(x,y)
        if ans==3:
            help()
            exit()
        if ans==4:
            exit()

        m.solveMazeAstar()
        m.printMaze()



if __name__ == '__main__':
    maze()
