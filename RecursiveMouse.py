import copy
from MazeBuilder import Maze

class Mouse:


  def __init__(self):
    # keeps track of number of solutions found
    self.solutions = 0

  def find_maze_paths(self, maze, start_row, start_col, exit_row, exit_col):
    # make a local copy of the maze as to not overwrite it and allow backtracking
    local_maze = copy.deepcopy( maze )
  
    # set the current position to visited
    if start_row == exit_row and start_col == exit_col:
      self.solutions += 1
      print("It's a path!!")
      print(local_maze)
      print()
    
    # recursive case
    else:
      if local_maze.get_value(start_row, start_col) != "@":
        local_maze.set_value(start_row, start_col, "!")

      # check spot above
      if local_maze.is_clear(start_row - 1, start_col):
        self.find_maze_paths(local_maze, start_row - 1, start_col, exit_row, exit_col)
      
      # check spot to the right
      if local_maze.is_clear(start_row, start_col + 1):
        self.find_maze_paths(local_maze, start_row, start_col + 1, exit_row, exit_col)
      
      # check spot below
      if local_maze.is_clear(start_row + 1, start_col):
        self.find_maze_paths(local_maze, start_row + 1, start_col, exit_row, exit_col)
      
      # check spot to the left
      if local_maze.is_clear(start_row, start_col - 1):
        self.find_maze_paths(local_maze, start_row, start_col - 1, exit_row, exit_col)
        
    
  def solution_found(self):
    return self.solutions > 0