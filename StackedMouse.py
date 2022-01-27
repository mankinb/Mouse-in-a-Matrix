from MazeBuilder import Maze
from StackADT import *

class Mouse:

  def __init__(self):
    self.solutions = 0
    self.solver = Stack()
    
  
  def pathfinder(self, maze, start_row, start_col, exit_row, exit_col):
    
    ''' 
    Functions similarly to RecursiveMouse, but instead uses stacks of tuples (row, column).
    '''

    self.solver.push((start_row, start_col))


    while not self.solver.isEmpty():
      current = self.solver.pop()
      if current[0] == exit_row and current[1] == exit_col:
        self.solutions += 1
        print("Success!")
        print("We found a path!")


        maze.set_value(start_row, start_col, "@")
        maze.set_value(exit_row, exit_col, "$")
        print(maze)

        break
      
      else:
        maze.set_value(current[0], current[1], "!")

        # check spot to the right
        if maze.is_clear(current[0], current[1] + 1):
          self.solver.push((current[0], current[1] + 1))

        # check spot to the left
        if maze.is_clear(current[0], current[1] - 1):
          self.solver.push((current[0], current[1] - 1))

        # check spot above
        if maze.is_clear(current[0] - 1, current[1]):
          self.solver.push((current[0] - 1, current[1]))

        # check spot below
        if maze.is_clear(current[0] + 1, current[1]):
          self.solver.push((current[0] + 1, current[1]))
        

  def solution_found(self):
    return self.solutions > 0

