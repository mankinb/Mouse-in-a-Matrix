#from mouserecursion import Mouse
from MazeBuilder import *
from RecursiveMouse import *

mouse = Mouse()
maze = Maze()

f_name = input( "Enter the name of the maze file (\"none\" if " \
		     + " using random file): ")

print()
if f_name != 'none':
  print( "loading " + f_name + " ...")
  maze.read_maze( f_name )
else:
  print("loading random maze...")
print()

print( '-------- The Original Maze --------' )
print()
print( maze )
print()

print("Row size:")
print(str(maze.get_row_size()) + " (0 - " + str(maze.get_row_size() - 1) + ")")
print()
print("Col size:")
print(str(maze.get_col_size()) + " (0 - " + str(maze.get_col_size() - 1) + ")")
print()
print()



invalid = True
while invalid:
  starting_row = int( input( 'Please enter the starting row : ' ) )
  print( starting_row )
  print()
  starting_col = int( input( 'Please enter the starting column : ' ) )
  print( starting_col )
  print()

  if maze.is_in_maze(starting_row, starting_col):
    if maze.is_clear(starting_row, starting_col):
      invalid = False
      maze.set_value(starting_row, starting_col, "@")
    else:
      print("Starting position is blocked.")
      print("Please choose another starting position...")
  else:
    print("Starting position is not in maze.")
    print("Please choose a position within")
    print("(0, 0) - (" + str(maze.get_row_size()) + ", " + str(maze.get_col_size) + ")...")

invalid = True
while invalid:
  exit_row = int( input( 'Please enter the exiting row : ' ) )
  print( exit_row )
  print()
  exit_col = int( input( 'Please enter the exiting column : ' ) )
  print( exit_col )
  print()

  if maze.is_in_maze(exit_row, exit_col):
    if maze.is_clear(exit_row, exit_col):
      invalid = False
      maze.set_value(exit_row, exit_col, "$")
    else:
      print("Exit position is blocked.")
      print("Please choose another exit position...")
  else:
    print("Exit position is not in maze.")
    print("Please choose a position within")
    print("(0, 0) - (" + str(maze.get_row_size()) + ", " + str(maze.get_col_size) + ")...")


print("Starting at (" + str(starting_row) + ", " + str(starting_col) + ") denoted by @")
print("Exiting at (" + str(exit_row) + ", " + str(exit_col) + ") denoted by $")
print()
mouse.find_maze_paths(maze, starting_row, starting_col, exit_row, exit_col)
if mouse.solution_found():
  print("Number of solutions found: " + str(mouse.solutions))
else:
  print("No solutions found to the maze --- maze is impossible.")
print()
