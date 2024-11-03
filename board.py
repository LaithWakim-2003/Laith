from cell import Cell
from colorama import Fore, Back, Style, init

from type import Empty, Iron, Magnet_Neg, Magnet_Pos, White_Circle
init()

class Board:
    
    def __init__(self, rows = 10 , cols = 10 , attempts = 10):
        self.rows = rows
        self.cols = cols
        self.attempts = attempts
        self.lm_grid = [[Cell() for _ in range(cols)] for _ in range(rows)]
    
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

    def choice(self):
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


        self.move_magnet(input_x, input_y, new_input_x, new_input_y)
        self.print_board()
        if self.win_condition():
            print("Congrats,You completed this level")
            return
        self.attempts -= 1
        print(f"Attempts left: {self.attempts}")

      if self.attempts == 0:
        print("No attempts left. Please restart the game.")


    def move_magnet(self, input_x, input_y, new_input_x, new_input_y):
      self.lm_grid[new_input_x][new_input_y].cell_type = self.lm_grid[input_x][input_y].cell_type
      self.lm_grid[input_x][input_y].cell_type = '.'
      if self.lm_grid[new_input_x][new_input_y].cell_type == 'R':
        self.move_cells_to_magnet(new_input_x, new_input_y)
      else:
        self.move_cells_away_from_magnet(new_input_x, new_input_y)
        
    def move_iron_away(self, start, end, step_for_x, step_for_y,mag_n_x,mag_n_y):
     if step_for_x in [-1,1]:
           y = mag_n_y
           step = step_for_x
     elif step_for_y in [-1,1]:
           step = step_for_y    
     for x in range(start, end, step):
        if step_for_y in [-1,1]:
           y = x
           x = mag_n_x
        if not self.is_within_bounds(x,y):
          continue     
        if self.lm_grid[x][y].cell_type == '.':
            pass
        elif self.lm_grid[x][y].cell_type in ['R', 'I']:
           if self.is_within_bounds(x + step_for_x, y + step_for_y):
            if self.lm_grid[x + step_for_x][y + step_for_y].cell_type == '.':
                self.lm_grid[x + step_for_x][y + step_for_y].cell_type = self.lm_grid[x][y].cell_type
                self.lm_grid[x][y].cell_type = '.'
                break
            elif self.lm_grid[x + step_for_x][y + step_for_y].cell_type in ['R', 'I']:
              if self.is_within_bounds(x + 2 * step_for_x, y + 2 * step_for_y):
                temporary = self.lm_grid[x + step_for_x][y + step_for_y].cell_type
                self.lm_grid[x + 2 * step_for_x][y + 2 * step_for_y].cell_type = self.lm_grid[x + step_for_x][y + step_for_y].cell_type
                self.lm_grid[x + step_for_x][y + step_for_y].cell_type = '.'
                self.lm_grid[x + 2 * step_for_x][y + 2 * step_for_y].cell_type = temporary
                self.lm_grid[x + step_for_x][y + step_for_y].cell_type = self.lm_grid[x][y].cell_type
                self.lm_grid[x][y].cell_type = '.'
                break
             
    def move_iron_towards(self, start , end , step_for_x, step_for_y,mag_x,mag_y):
      if step_for_x in [-1,1]:
           y = mag_y
           step = step_for_x
      elif step_for_y in [-1,1]:
           step = step_for_y    
      for x in range(start, end, step):
         if step_for_y in [-1,1]:
           y = x
           x = mag_x
         if self.lm_grid[x][y].cell_type == '.':
            if self.lm_grid[x + step_for_x][y + step_for_y].cell_type == '.':
               pass
            elif self.lm_grid[x + step_for_x][y + step_for_y].cell_type in ['N','I']:
                temp = self.lm_grid[x][y].cell_type
                self.lm_grid[x][y].cell_type = self.lm_grid[x + step_for_x][y + step_for_y].cell_type
                self.lm_grid[x + step_for_x][y + step_for_y].cell_type = temp
         else:
            self.lm_grid[x][y].cell_type in ['N','I']
            pass
       
    def move_cells_to_magnet(self , mag_x , mag_y):
    # Up => down
      self.move_iron_towards(mag_x - 1, 0,-1,0,mag_x,mag_y)
    # Down => up
      self.move_iron_towards(mag_x + 1,self.rows - 1,1,0,mag_x,mag_y)
    # Left => right
      self.move_iron_towards(mag_y - 1,0,0,-1,mag_x,mag_y)
    # Right => left
      self.move_iron_towards(mag_y + 1,self.cols - 1,0,1,mag_x,mag_y)

    def move_cells_away_from_magnet(self, mag_n_x, mag_n_y):
    # Up direction
     self.move_iron_away(mag_n_x - 1 , -1 , -1 , 0,mag_n_x,mag_n_y)
    # Down direction
     self.move_iron_away(mag_n_x + 1 , self.rows - 1 , 1 , 0,mag_n_x,mag_n_y)
    # Left direction
     self.move_iron_away(mag_n_y - 1 , -1 , 0 ,-1,mag_n_x,mag_n_y)
    # Right direction
     self.move_iron_away(mag_n_y + 1 , self.cols - 1 , 0 , 1 ,mag_n_x, mag_n_y)

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
        