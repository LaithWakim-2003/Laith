from algo import Algo
from availablemoves import AvailableMoves
from cell import Cell
from colorama import Fore, Back, Style, init

from movement import Movement
from type import Empty, Iron, Magnet_Neg, Magnet_Pos, Normal_Cell, White_Circle
init()

class Board:
    my_grids = []
    def __init__(self, rows = 10 , cols = 10 , attempts = 10):
        self.rows = rows
        self.cols = cols
        self.attempts = attempts
        self.lm_grid = [[Normal_Cell(x,y,white_space=False) for x in range(cols)] for y in range(rows)]
    
    def get_magnet_position(self):
       input_x = int(input("Enter x coordinate: "))
       if input_x == 28:
         return 
       input_y = int(input("Enter y coordinate: ")) 
       return input_x, input_y 
    
    def get_new_position(self): 
       new_input_x = int(input("Enter new x coordinate: ")) 
       new_input_y = int(input("Enter new y coordinate: ")) 
       return new_input_x, new_input_y
     
    def is_within_bounds(self, x, y): 
       return 0 <= x < self.rows and 0 <= y < self.cols 
    
    def is_magnet(self, x, y): 
       return self.lm_grid[x][y].cell_type in ['R', 'N'] 
    
    def is_invalid_destination(self, x, y): 
       return self.lm_grid[x][y].cell_type in [' ', 'R', 'N', 'I']
     
    def place_normal_cell(self,n_cell_x,n_cell_y,white_space):
        cell = Normal_Cell(n_cell_x,n_cell_y,white_space = white_space)
        self.lm_grid[n_cell_x][n_cell_y] = cell
        
    def place_magnet_pos(self, mag_x, mag_y,white_space):
      magnet_pos = Magnet_Pos(mag_x,mag_y,white_space)
      self.lm_grid[mag_x][mag_y] = magnet_pos

    def place_magnet_neg(self,mag_n_x,mag_n_y,white_space):
      magnet_neg = Magnet_Neg(mag_n_x,mag_n_y,white_space)
      self.lm_grid[mag_n_x][mag_n_y] = magnet_neg

    def place_empty_cell(self,empty_x,empty_y,white_space):
       empty = Empty(empty_x,empty_y,white_space)
       self.lm_grid[empty_x][empty_y] = empty

    def place_iron(self, iron_x,iron_y,white_space):
        iron = Iron(iron_x,iron_y,white_space)
        self.lm_grid[iron_x][iron_y] = iron

    def place_white_circle(self, white_cicle_pos_x, white_cicle_pos_y,white_space = True):
        white_space = White_Circle(white_cicle_pos_x, white_cicle_pos_y,white_space)
        self.lm_grid[white_cicle_pos_x][white_cicle_pos_y] = white_space
        
    def choice(self,board):
      self.print_board()
      print(f"Attempts: {self.attempts}")
      while self.attempts > 0:
        input_x, input_y = self.get_magnet_position()
        if not self.is_within_bounds(input_x, input_y) or not self.is_magnet(input_x, input_y):
            print("Invalid")
            continue
          
        new_input_x, new_input_y = self.get_new_position()
        if not self.is_within_bounds(new_input_x, new_input_y) or self.is_invalid_destination(new_input_x, new_input_y):
            print("Invalid Position")
            continue


        self.move_magnet(board,input_x, input_y, new_input_x, new_input_y)
        self.print_board()
        if self.win_condition():
            print("Congrats,You completed this level")
            return
        self.attempts -= 1
        print(f"Attempts left: {self.attempts}")

      if self.attempts == 0:
        print("No attempts left. Please restart the game.")


    def move_magnet(self,board, input_x, input_y, new_input_x, new_input_y):
      self.lm_grid[new_input_x][new_input_y].cell_type = self.lm_grid[input_x][input_y].cell_type
      self.lm_grid[input_x][input_y].cell_type = '.'
      if self.lm_grid[input_x][input_y].white_space == True:
        Movement().place_normal_cell(board,input_x,input_y,True)
      else:
        Movement().place_normal_cell(board,input_x,input_y,False)  
        
      if self.lm_grid[new_input_x][new_input_y].cell_type == 'R':
         if self.lm_grid[new_input_x][new_input_y].white_space == True:
            Movement().place_magnet_pos(board,new_input_x,new_input_y,True)
         else:
            Movement().place_magnet_pos(board,new_input_x,new_input_y,False)
         Movement().move_cells_to_magnet(board,new_input_x, new_input_y,board.rows,board.cols)
      else:
         if self.lm_grid[new_input_x][new_input_y].white_space == True:
            Movement().place_magnet_neg(board,new_input_x,new_input_y,True)
         else:
            Movement().place_magnet_neg(board,new_input_x,new_input_y,False)
         Movement().move_cells_away_from_magnet(board,new_input_x, new_input_y,board.rows,board.cols)
      
    def win_condition(self):
       winner = True     
       for row in range(self.rows):
        for col in range(self.cols):
            if self.lm_grid[row][col].white_space == True:
              if self.lm_grid[row][col].cell_type in ['I','N','R']: 
                pass
              else:
                winner = False
            else:
              continue      
       return winner 
              
    def print_board(self):
      col_indices = 'X\\Y  ' + '  '.join([str(i) for i in range(self.cols)])
      print(col_indices)

      for idx, row in enumerate(self.lm_grid):
        row_str = '  '.join([
            (Back.GREEN + cell.cell_type + Back.RESET) if cell.white_space 
            else (Fore.RED + cell.cell_type + Fore.RESET) if cell.cell_type == 'R' 
            else (Fore.BLUE + cell.cell_type + Fore.RESET) if cell.cell_type == 'N' 
            else (Fore.YELLOW + cell.cell_type + Fore.RESET) if cell.cell_type == 'I' 
            else (Fore.BLACK + cell.cell_type + Fore.RESET) if cell.cell_type == ' ' 
            else '.' for cell in row
        ])
        print(f" {idx}   {row_str}")
        
    def print_board_type(self):
      col_indices = 'X\\Y  ' + '  '.join([str(i) for i in range(self.cols)])
      print(col_indices)

      for idx, row in enumerate(self.lm_grid):
        row_str = '  '.join([
            (Back.GREEN + type(cell).__name__ + Back.RESET) if cell.white_space 
            else (Fore.RED + type(cell).__name__ + Fore.RESET) if cell.cell_type == 'R' 
            else (Fore.BLUE + type(cell).__name__ + Fore.RESET) if cell.cell_type == 'N' 
            else (Fore.YELLOW + type(cell).__name__ + Fore.RESET) if cell.cell_type == 'I' 
            else (Fore.BLACK + type(cell).__name__ + Fore.RESET) if cell.cell_type == ' ' 
            else type(cell).__name__ for cell in row
        ])
        print(f" {idx}   {row_str}")
