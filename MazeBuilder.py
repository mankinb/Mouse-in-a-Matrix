import random

class Maze:

    def __init__(self, max_row = 12, max_sol = 12):
        """Create a maze"""
        self.MAXROW = max_row
        self.MAXCOL = max_sol
        self.POSSIBLEPATH = ' '
        self.BLOCKER      = '*'
        self.THEWAYOUT    = '!'

        self.PATH_BLOCKER_RATIO = 0.5

        self.the_maze = self._gen_maze()


    def _gen_maze(self):

        """Generate a random maze based on probability"""
        local_maze = [['*' for i in range( self.MAXCOL  )] \
                         for j in range( self.MAXROW )]

        for row in range( self.MAXROW ):
            for col in range( self.MAXCOL ):
                threshold = random.random()
                if threshold > self.PATH_BLOCKER_RATIO:
                    local_maze[row][col] = self.POSSIBLEPATH
                else:
                    local_maze[row][col] = self.BLOCKER

        return local_maze

    
    def __str__(self):

        """Generate a string representation of the maze"""
        maze_str = " "
        for i in range(self.get_col_size()):
          maze_str += str(i % 10)
        maze_str += "\n"
        #print(self.the_maze)
        for i in range(self.get_row_size()):
          maze_str += str(i % 10)
          for j in range(self.get_col_size()):
            maze_str += self.the_maze[i][j]
          maze_str += "\n"
        maze_str = maze_str.strip("\n")
        
        return maze_str
        

    def get_col_size(self):

        """Return column count.  
        Note: Mazes will not all be self.MAXROW by self.MAXCOL"""
        return len(self.the_maze[0])


    def get_row_size(self):

        """Return row count"""
        return len(self.the_maze)


    def read_maze(self, file_name):

        """Reading maze from a file.
           The file should be in the form of a matrix, e.g.,
           ** *
           *  *
           ** *
           ** *
           would be a 4x4 input maze."""
        file = open(file_name, "rt")
        lines = file.readlines()
        result = []
        for i in range(len(lines)):
          currentline = []
          currentline[:0] = lines[i].strip('\n')
          result.append(currentline)
        self.the_maze = result


    def get_maze(self):

        """Return a copy of the maze attribute
            this is a one-liner method """
        return self.the_maze


    def is_clear(self, row, col):

        """Return True if this cell is clear (pathway)."""
        if self.is_in_maze(row, col):
          if self.the_maze[row][col] in [" ", "$"]:
            return True
        return False


    def is_in_maze(self, row, col):

        """Return True if a cell is inside the maze."""
        if row in range(self.get_row_size()) and col in range(self.get_col_size()):
          return True
        else:
          return False


    def set_value(self, row, col, value):

        """Set the value to a cell in the maze
           For example, you will use this method to set the value of a cell to !, indicating that it has been visited """   
        self.the_maze[row][col] = str(value)


    def get_value(self, row, col):
        
        """Return the value of the current cell."""
        return self.the_maze[row][col]

