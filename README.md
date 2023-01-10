# MAZE SOLVER
Maze solver made in python
<!-- TOC -->
# Description
  This python script solves mazes - finds and marks shortest path from start to end of a maze using A* (A star) algorithm.
  I tested it for mazes up to size of 150x150. For mazes bigger than 100x100 it takes considerable amount of time to execute. I didn’t use any maze library because I wanted to try to implement everything on my own.
# How to use it
  You can either chose to solve maze created by yourself - from .txt file or solve randomly generated maze which program generates. There is a baisc menu in which you can choose your preferences by typing in number coresponding to option.
  
  #Menu:
  
    ###########[MAZE SOLVER]###########
    1. Solve maze loaded from from file 
    2. Solve randomly generated maze
    3. Help
    4. Exit
    #######[IGOR NIEBYLSKI 2023]#######
    
    
  #Maze .txt file template:
  
  
        # - walls
         - passgaes (whitespaces)
        e - exit (only one)
        s - start (only one)
        Example maze:
        #e#####
        # #   #
        #     #
        #  #  #
        # ### #
        #  #  #
        #     #
        #   # #
        #####s#
        
