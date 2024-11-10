from type import Empty, Iron, Magnet_Neg, Magnet_Pos, Normal_Cell, White_Circle


class Movement:
    def place_normal_cell(self,board,n_cell_x,n_cell_y,white_space):
        cell = Normal_Cell(n_cell_x,n_cell_y,white_space = white_space)
        board.lm_grid[n_cell_x][n_cell_y] = cell
        
    def place_magnet_pos(self,board, mag_x, mag_y,white_space):
      magnet_pos = Magnet_Pos(mag_x,mag_y,white_space)
      board.lm_grid[mag_x][mag_y] = magnet_pos

    def place_magnet_neg(self,board,mag_n_x,mag_n_y,white_space):
      magnet_neg = Magnet_Neg(mag_n_x,mag_n_y,white_space)
      board.lm_grid[mag_n_x][mag_n_y] = magnet_neg

    def place_empty_cell(self,board,empty_x,empty_y,white_space):
       empty = Empty(empty_x,empty_y,white_space)
       board.lm_grid[empty_x][empty_y] = empty

    def place_iron(self,board, iron_x,iron_y,white_space):
        iron = Iron(iron_x,iron_y,white_space)
        board.lm_grid[iron_x][iron_y] = iron

    def place_white_circle(self,board, white_cicle_pos_x, white_cicle_pos_y,white_space = True):
        white_space = White_Circle(white_cicle_pos_x, white_cicle_pos_y,white_space)
        board.lm_grid[white_cicle_pos_x][white_cicle_pos_y] = white_space
        
        
    def move_iron_away(self,board, start, end, step_for_x, step_for_y,mag_n_x,mag_n_y):
     if step_for_x in [-1,1]:
           y = mag_n_y
           step = step_for_x
     elif step_for_y in [-1,1]:
           step = step_for_y    
     for x in range(start, end, step):
        if step_for_y in [-1,1]:
           y = x
           x = mag_n_x
        if not self.is_within_bounds(x,y,board.rows,board.cols):
          continue     
        if board.lm_grid[x][y].cell_type == '.':
            pass
        elif board.lm_grid[x][y].cell_type in ['R', 'I']:
           if self.is_within_bounds(x + step_for_x, y + step_for_y,board.rows,board.cols):
            if board.lm_grid[x + step_for_x][y + step_for_y].cell_type == '.':
                board.lm_grid[x + step_for_x][y + step_for_y].cell_type = board.lm_grid[x][y].cell_type
                if board.lm_grid[x + step_for_x][y + step_for_y].cell_type == 'R':
                   if board.lm_grid[x + step_for_x][y + step_for_y].white_space == True:
                       self.place_magnet_pos(board,x + step_for_x,y + step_for_y,True)
                   else:
                       self.place_magnet_pos(board,x + step_for_x,y + step_for_y,False)
                elif board.lm_grid[x + step_for_x][y + step_for_y].cell_type == 'I': 
                   if board.lm_grid[x + step_for_x][y + step_for_y].white_space == True:
                       self.place_iron(board,x + step_for_x,y + step_for_y,True)
                   else:
                       self.place_iron(board,x + step_for_x,y + step_for_y,False)
                board.lm_grid[x][y].cell_type = '.'
                if board.lm_grid[x][y].white_space == True:
                    self.place_normal_cell(board,x,y,True)
                else:
                    self.place_normal_cell(board,x,y,False)
                break
            elif board.lm_grid[x + step_for_x][y + step_for_y].cell_type in ['R', 'I']:
              if self.is_within_bounds(x + 2 * step_for_x, y + 2 * step_for_y,board.rows,board.cols):
                temporary = board.lm_grid[x + step_for_x][y + step_for_y].cell_type
                board.lm_grid[x + 2 * step_for_x][y + 2 * step_for_y].cell_type = board.lm_grid[x + step_for_x][y + step_for_y].cell_type
                if board.lm_grid[x + 2 * step_for_x][y + 2 * step_for_y].cell_type == 'R':
                   if board.lm_grid[x + 2 * step_for_x][y + 2 * step_for_y].white_space == True:
                       self.place_magnet_pos(board,x + 2 * step_for_x,y + 2 * step_for_y,True)
                   else:
                       self.place_magnet_pos(board,x + 2 * step_for_x,y + 2 * step_for_y,False)
                elif board.lm_grid[x + 2 * step_for_x][y + 2 * step_for_y].cell_type == 'I': 
                   if board.lm_grid[x + 2 * step_for_x][y + 2 * step_for_y].white_space == True:
                       self.place_iron(board,x + 2 * step_for_x,y + 2 * step_for_y,True)
                   else:
                       self.place_iron(board,x + 2 * step_for_x,y + 2 * step_for_y,False)
                board.lm_grid[x + step_for_x][y + step_for_y].cell_type = '.'
                if board.lm_grid[x + step_for_x][y + step_for_y].white_space == True:
                    self.place_normal_cell(board,x + step_for_x,y + step_for_y,True)
                else:
                    self.place_normal_cell(board,x + step_for_x,y + step_for_y,False)
                
                board.lm_grid[x + 2 * step_for_x][y + 2 * step_for_y].cell_type = temporary
                board.lm_grid[x + step_for_x][y + step_for_y].cell_type = board.lm_grid[x][y].cell_type
                if board.lm_grid[x +  step_for_x][y + step_for_y].cell_type == 'R':
                   if board.lm_grid[x +  step_for_x][y + step_for_y].white_space == True:
                       self.place_magnet_pos(board,x +  step_for_x,y + step_for_y,True)
                   else:
                       self.place_magnet_pos(board,x +  step_for_x,y + step_for_y,False)
                elif board.lm_grid[x +  step_for_x][y + step_for_y].cell_type == 'I': 
                   if board.lm_grid[x +  step_for_x][y + step_for_y].white_space == True:
                       self.place_iron(board,x +  step_for_x,y + step_for_y,True)
                   else:
                       self.place_iron(board,x +  step_for_x,y + step_for_y,False)
                board.lm_grid[x][y].cell_type = '.'
                if board.lm_grid[x][y].white_space == True:
                    self.place_normal_cell(board,x,y,True)
                else:
                    self.place_normal_cell(board,x,y,False)
                break
             
    def move_iron_towards(self,board, start , end , step_for_x, step_for_y,mag_x,mag_y):
      if step_for_x in [-1,1]:
           y = mag_y
           step = step_for_x
      elif step_for_y in [-1,1]:
           step = step_for_y    
      for x in range(start, end, step):
         if step_for_y in [-1,1]:
           y = x
           x = mag_x
         if board.lm_grid[x][y].cell_type == '.':
            if board.lm_grid[x + step_for_x][y + step_for_y].cell_type == '.':
               pass
            elif board.lm_grid[x + step_for_x][y + step_for_y].cell_type in ['N','I']:
                temp = board.lm_grid[x][y].cell_type
                board.lm_grid[x][y].cell_type = board.lm_grid[x + step_for_x][y + step_for_y].cell_type
                if board.lm_grid[x][y].cell_type == 'N':
                   if board.lm_grid[x][y].white_space == True:
                       self.place_magnet_neg(board,x,y,True)
                   else:
                       self.place_magnet_neg(board,x,y,False)
                elif board.lm_grid[x][y].cell_type == 'I': 
                   if board.lm_grid[x][y].white_space == True:
                       self.place_iron(board,x,y,True)
                   else:
                       self.place_iron(board,x,y,False)
                board.lm_grid[x + step_for_x][y + step_for_y].cell_type = temp
                if board.lm_grid[x+step_for_x][y+step_for_y].cell_type == 'N':
                   if board.lm_grid[x+step_for_x][y+step_for_y].white_space == True:
                       self.place_magnet_neg(board,x+step_for_x,y+step_for_y,True)
                   else:
                       self.place_magnet_neg(board,x+step_for_x,y+step_for_y,False)
                elif board.lm_grid[x+step_for_x][y+step_for_y].cell_type == 'I': 
                   if board.lm_grid[x+step_for_x][y+step_for_y].white_space == True:
                       self.place_iron(board,x+step_for_x,y+step_for_y,True)
                   else:
                       self.place_iron(board,x+step_for_x,y+step_for_y,False)
                elif board.lm_grid[x+step_for_x][y+step_for_y].cell_type == '.': 
                   if board.lm_grid[x+step_for_x][y+step_for_y].white_space == True:
                       self.place_normal_cell(board,x+step_for_x,y+step_for_y,True)
                   else:
                       self.place_normal_cell(board,x+step_for_x,y+step_for_y,False)       
         else:
            board.lm_grid[x][y].cell_type in ['N','I']
            pass
       
    def move_cells_to_magnet(self ,board, mag_x , mag_y,rows,cols):
    # Up => down
      self.move_iron_towards(board,mag_x - 1, 0,-1,0,mag_x,mag_y)
    # Down => up
      self.move_iron_towards(board,mag_x + 1,rows - 1,1,0,mag_x,mag_y)
    # Left => right
      self.move_iron_towards(board,mag_y - 1,0,0,-1,mag_x,mag_y)
    # Right => left
      self.move_iron_towards(board,mag_y + 1,cols - 1,0,1,mag_x,mag_y)

    def move_cells_away_from_magnet(self, board,mag_n_x, mag_n_y,rows,cols):
    # Up direction
     self.move_iron_away(board,mag_n_x - 1 , -1 , -1 , 0,mag_n_x,mag_n_y)
    # Down direction
     self.move_iron_away(board,mag_n_x + 1 , rows - 1 , 1 , 0,mag_n_x,mag_n_y)
    # Left direction
     self.move_iron_away(board,mag_n_y - 1 , -1 , 0 ,-1,mag_n_x,mag_n_y)
    # Right direction
     self.move_iron_away(board,mag_n_y + 1 , cols - 1 , 0 , 1 ,mag_n_x, mag_n_y)
     
     
    def is_within_bounds(self, x, y,rows,cols): 
       return 0 <= x < rows and 0 <= y < cols 
    
    def is_magnet(self, x, y): 
       return self.lm_grid[x][y].cell_type in ['R', 'N'] 
    
    def is_invalid_destination(self, x, y): 
       return self.lm_grid[x][y].cell_type in [' ', 'R', 'N', 'I']
     