from colorama import Back, Fore
from availablemoves import AvailableMoves
import availablemoves
from movement import Movement
import copy

class Algo:
    my_grids = []
    stack = []
    visited = set()
    def setterboard(self,board):
        self.my_grids.append(board)
        self.dfs(board)
        
    def visited_checker(self, board):
        for visited_board in self.visited:  # Iterate through each visited board
            is_different = False  # Flag to check if boards are different
            for x in range(board.rows):
                for y in range(board.cols):
                    if board.lm_grid[x][y].cell_type == visited_board.lm_grid[x][y].cell_type:
                        continue
                    else:  # If a mismatch is found
                        is_different = True
                        break  # Break out of the inner loop
                if is_different:
                    break  # Break out of the outer loop
            if not is_different:
                return True  # Board is already visited
        return False  # Board is not visited


    def dfs(self, start_board):
      # Initialize the stack with the starting board
        stack = [start_board]
        while stack:
            board = stack.pop() # Pop the current board from the stack 
        # Check for win condition 
            if self.win_condition(board):
               print("WINNER BOARD")
               self.print_board(board)
               return True
             # Check if the board has already been visited
            if self.visited_checker(board):
               print("VISITED!!!")
               self.print_board(board)
               continue 
             # Mark the board as visited 
            self.visited.add(board) 
           
      
      ## if is win return winning state
      ##  if  visited   continue
      ## if not visited  add to  visited == > check (كل الحالات) ==> for استدعاء عودي بالحالة الجديدة لكل الحالات send new board in parameter
      # for index,grid in enumerate(self.my_grids):
      #     print(f"depth {index}")
      #     winner = self.win_condition(grid)
      #     if winner == True:
      #        print("WINNER BOARD")
      #        self.print_board(grid)
      #        break
           
      #     if self.visited_checker(grid):
      #       print("VISITED!!!")
      #       self.print_board(grid)
      #       continue
          
      #     else:
      #       self.visited.add(board)
      #       self.check_magnet_position(board)
      
    def check_magnet_position(self,board):
        found_magnet = False
        for x in range(board.rows):
          for y in range(board.cols):
            if board.lm_grid[x][y].cell_type in ['R']:
              # my_magnet = Magnet_Pos(x,y)
               my_magnet_x = x
               my_magnet_y = y
               found_magnet = True
               break
            elif board.lm_grid[x][y].cell_type in ['N']:
                my_magnet_x = x
                my_magnet_y = y
                found_magnet = True
                break
            else:
               continue
        if found_magnet:
           self.check_available_moves(my_magnet_x,my_magnet_y,board)
        else:
           print("There is no magnet in this board")    
             
    def check_available_moves(self,magnet_x,magnet_y,board):
        my_available_moves_list = []
        for x in range(board.rows):
          for y in range(board.cols):
            #add an if statement for cells with cell type . only
            if board.lm_grid[x][y].cell_type == '.':
              available_moves = AvailableMoves(
              magnet_x = magnet_x,
              magnet_y = magnet_y,
              available_x = x,
              available_y = y
              )
              my_available_moves_list.append(available_moves)
        for move in my_available_moves_list:
          # print(move)
            self.create_new_board(board,my_available_moves_list)
        
    def create_new_board(self,board,my_available_moves_list):
        from board import Board
        for move in my_available_moves_list:
          new_board = Board(board.rows,board.cols)
          for row in range(board.rows):
            for col in range(board.cols):
              
              #new_board.lm_grid[row][col] = board[row][col]
              #new_board.lm_grid[row][col].cell_type = board[row][col].cell_type
              new_board.lm_grid[row][col] = copy.deepcopy(board.lm_grid[row][col])
              #self.my_grids.append(new_board.lm_grid)
          self.move_magnet(new_board, move.magnet_x, move.magnet_y, move.available_x, move.available_y)
          self.print_board(new_board)
          #self.print_board_type(new_board)
          self.my_grids.append(new_board)
          
    def move_magnet(self,new_board, input_x, input_y, new_input_x, new_input_y):
      print(f"input_x = {input_x} input_y = {input_y} new_input_x = {new_input_x} new_input_y = {new_input_y}")
      
      if new_board.lm_grid[input_x][input_y].cell_type in ['R']:
         if new_board.lm_grid[new_input_x][new_input_y].white_space == True:
            Movement().place_magnet_pos(new_board,new_input_x,new_input_y,True)
         else:
            Movement().place_magnet_pos(new_board,new_input_x,new_input_y,False)
         Movement().move_cells_to_magnet(new_board,new_input_x,new_input_y,new_board.rows,new_board.cols)  ##################  
      elif new_board.lm_grid[input_x][input_y].cell_type in ['N']:
         if new_board.lm_grid[new_input_x][new_input_y].white_space == True:
            Movement().place_magnet_neg(new_board,new_input_x,new_input_y,True)
         else:
             Movement().place_magnet_neg(new_board,new_input_x,new_input_y,False)
         Movement().move_cells_away_from_magnet(new_board,new_input_x,new_input_y,new_board.rows,new_board.cols)  ##################
      if new_board.lm_grid[input_x][input_y].white_space == True:       
         Movement().place_normal_cell(new_board,input_x,input_y,True)
      else:
        Movement().place_normal_cell(new_board,input_x,input_y,False)
      
      
      
      
    def print_board(self,new_board):
      col_indices = 'X\\Y  ' + '  '.join([str(i) for i in range(new_board.cols)])
      print(col_indices)

      for idx, row in enumerate(new_board.lm_grid):
        row_str = '  '.join([
            (Back.GREEN + cell.cell_type + Back.RESET) if cell.white_space 
            else (Fore.RED + cell.cell_type + Fore.RESET) if cell.cell_type == 'R' 
            else (Fore.BLUE + cell.cell_type + Fore.RESET) if cell.cell_type == 'N' 
            else (Fore.YELLOW + cell.cell_type + Fore.RESET) if cell.cell_type == 'I' 
            else (Fore.BLACK + cell.cell_type + Fore.RESET) if cell.cell_type == ' ' 
            else '.' for cell in row
        ])
        print(f" {idx}   {row_str}")
      print("----------------------------------")
        
        
    def print_board_type(self,new_board):
      col_indices = 'X\\Y  ' + '  '.join([str(i) for i in range(new_board.cols)])
      print(col_indices)

      for idx, row in enumerate(new_board.lm_grid):
        row_str = '  '.join([
            (Back.GREEN + type(cell).__name__ + Back.RESET) if cell.white_space 
            else (Fore.RED + type(cell).__name__ + Fore.RESET) if cell.cell_type == 'R' 
            else (Fore.BLUE + type(cell).__name__ + Fore.RESET) if cell.cell_type == 'N' 
            else (Fore.YELLOW + type(cell).__name__ + Fore.RESET) if cell.cell_type == 'I' 
            else (Fore.BLACK + type(cell).__name__ + Fore.RESET) if cell.cell_type == ' ' 
            else type(cell).__name__ for cell in row
        ])
        print(f" {idx}   {row_str}")
      print("----------------------------------")
      print("----------------------------------")
      
    def win_condition(self,board):
       winner = True     
       for row in range(board.rows):
        for col in range(board.cols):
            if board.lm_grid[row][col].white_space == True:
              if board.lm_grid[row][col].cell_type in ['I','N','R']: 
                pass
              else:
                winner = False
            else:
              continue      
       return winner 
