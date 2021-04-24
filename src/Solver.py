# Solver 2021
# Template for the algorithm to solve a sudoku. Builds a recursive backtracking solution
# that branches on possible values that could be placed in the next empty cell. 
# Initial pruning of the recursion tree - 
#       we don't continue on any branch that has already produced an inconsistent solution
#       we stop and return a complete solution once one has been found

import pygame, Sudoku_IO

def solve(snapshot, screen):
    # display current snapshot
    pygame.time.delay(200)
    Sudoku_IO.displayPuzzle(snapshot, screen)
    pygame.display.flip()
    # if current snapshot is complete ... return a value
    # if current snapshot not complete ...
    # for each possible value for an empty cell
    #    clone current snapshot and update it, 
    #    if new snapshot is consistent, perform recursive call
    # return a value
    

# Check whether a snapshot is consistent, i.e. all cell values comply 
# with the sudoku rules (each number occurs only once in each block, row and column).
def checkConsistency(snapshot):
    return True

# Check whether a puzzle is solved. 
# return true if the sudoku is solved, false otherwise
def isComplete(snapshot):
    return True

