from bfs import BFS
from dfs import DFS
from board import Board

class Type:
    def __init__(self,board):
        c = str(input("Please choose BFS or DFS: "))
        if c == 'BFS':
            BFS().setterboard(board)
        elif c == 'DFS':
            DFS().setterboard(board)         
        else:
            board.choice(board)
class Level1:

    def __init__(self):
        self.board = Board(rows=3, cols=4,attempts=5)
        self.board.place_magnet_neg(2, 0,False)
        self.board.place_iron(1, 2,False)
        self.board.place_white_circle(1,1,True)
        self.board.place_white_circle(1,3,True)

        Type(self.board)
        
class Level2:

    def __init__(self):
        self.board = Board(rows=5, cols=5,attempts=5)
        self.board.place_iron(2, 1,False)
        self.board.place_iron(1, 2,False)
        self.board.place_iron(2, 3,False)
        self.board.place_iron(3, 2,False)
        self.board.place_white_circle(0, 2,True)
        self.board.place_white_circle(2, 0,True)
        self.board.place_white_circle(2, 2,True)
        self.board.place_white_circle(2, 4,True)
        self.board.place_white_circle(4, 2,True)
        self.board.place_magnet_neg(4, 0,False)

        Type(self.board)


class Level3:

    def __init__(self):
        self.board = Board(rows=3, cols=4,attempts=5)
        self.board.place_empty_cell(0,0,False)
        self.board.place_empty_cell(0,1,False)
        self.board.place_empty_cell(0,2,False)
        self.board.place_iron(1, 2,False)
        self.board.place_white_circle(0, 3,True)
        self.board.place_white_circle(2, 3,True)
        self.board.place_magnet_neg(2, 0,False)

        Type(self.board)

class Level4:

    def __init__(self):
        self.board = Board(rows=5, cols=3,attempts=2)
        self.board.place_empty_cell(1,0,False)
        self.board.place_empty_cell(3,0,False)
        self.board.place_iron(1, 1,False)
        self.board.place_iron(3, 1,False)
        self.board.place_white_circle(0, 0,True)
        self.board.place_white_circle(0, 2,True)
        self.board.place_white_circle(4, 1,True)
        self.board.place_magnet_neg(2, 0,False)

        Type(self.board)

class Level5:
    def __init__(self):
        self.board = Board(rows=4, cols=3,attempts=2)
        self.board.place_empty_cell(0,1,False)
        self.board.place_empty_cell(1,1,False)
        self.board.place_empty_cell(2,1,False)
        self.board.place_iron(1, 0,True)
        self.board.place_iron(2, 0,False)
        self.board.place_iron(1, 2,True)
        self.board.place_iron(2, 2,False)
        self.board.place_white_circle(0, 0,True)
        self.board.place_white_circle(0, 2,True)
        self.board.place_white_circle(3, 0,True)
        self.board.place_magnet_neg(3, 1,False)

        Type(self.board)

class Level6:

    def __init__(self):
        self.board = Board(rows=3, cols=5,attempts=2)
        self.board.place_magnet_neg(2, 0,False)
        self.board.place_iron(1, 1,False)
        self.board.place_iron(1, 3,False)
        self.board.place_white_circle(1,2,True)
        self.board.place_white_circle(0,3,True)
        self.board.place_white_circle(2,3,True)

        Type(self.board)

class Level7:

    def __init__(self):
        self.board = Board(rows=5, cols=4,attempts=2)
        self.board.place_white_circle(0,0,True)
        self.board.place_iron(1, 0,True)
        self.board.place_iron(2, 0,False)
        self.board.place_iron(3, 1,False)
        self.board.place_iron(3, 2,True)
        self.board.place_magnet_neg(2, 1,False)
        self.board.place_white_circle(2,3,True)
        self.board.place_white_circle(4,3,True)
        self.board.place_empty_cell(4,0,False)
        self.board.place_empty_cell(4,1,False)
        self.board.place_empty_cell(4,2,False)

        Type(self.board)

class Level8:

    def __init__(self):
        self.board = Board(rows=3, cols=4,attempts=2)
        self.board.place_magnet_neg(2, 0,False)
        self.board.place_iron(1, 1,False)
        self.board.place_iron(1, 2,False)

        self.board.place_white_circle(0,0,True)
        self.board.place_white_circle(0,2,True)
        self.board.place_white_circle(2,2,True)

        Type(self.board)

                

class Level9:

    def __init__(self):
        self.board = Board(rows=1, cols=7,attempts=2)
        self.board.place_magnet_neg(0, 0,False)
        self.board.place_white_circle(0, 1,True)
        self.board.place_iron(0, 3,True)

        self.board.place_iron(0,5,False)
        self.board.place_white_circle(0,6,True)
        

        Type(self.board)


class Level10:

    def __init__(self):
        self.board = Board(rows=4, cols=4,attempts=2)
        self.board.place_magnet_neg(0, 0,False)
        self.board.place_white_circle(1, 1,True)
        self.board.place_white_circle(1, 3,True)

        self.board.place_iron(2, 2,False)
        self.board.place_iron(2, 3,False)

        self.board.place_white_circle(3, 0,True)
        self.board.place_iron(3,1,False)
        self.board.place_white_circle(3,3,True)
        

        Type(self.board)

                        

class Level11:

    def __init__(self):
        self.board = Board(rows=2, cols=5,attempts=1)
        self.board.place_white_circle(0, 1,True)
        self.board.place_white_circle(0, 2,True)
        self.board.place_white_circle(0, 3,True)

        self.board.place_iron(0, 0,False)
        self.board.place_iron(0, 4,False)

        self.board.place_magnet_pos(1,2,False)
        self.board.place_empty_cell(1,0,False)
        self.board.place_empty_cell(1,1,False)
        self.board.place_empty_cell(1,3,False)
        self.board.place_empty_cell(1,4,False)

        Type(self.board)

        
        

class Level12:

    def __init__(self):
        self.board = Board(rows=5, cols=4,attempts=1)
       
        self.board.place_iron(0, 0,False)
        self.board.place_iron(1, 0,True)
        self.board.place_iron(4, 3,False)
        self.board.place_white_circle(2,0,True)
        self.board.place_white_circle(4, 0,True)
        self.board.place_white_circle(4, 2,True)
        self.board.place_magnet_pos(3,1,False)
        self.board.place_empty_cell(0,2,False)
        self.board.place_empty_cell(0,3,False)
        self.board.place_empty_cell(1,2,False)
        self.board.place_empty_cell(1,3,False)

        Type(self.board)

class Level13:
    
    def __init__(self):
        self.board = Board(rows=3, cols=6,attempts=2)
        self.board.place_iron(0, 0,False)
        self.board.place_iron(0, 4,True)
        self.board.place_iron(0, 5,False)
        self.board.place_white_circle(0,3,True)
        self.board.place_white_circle(1,1,True)
        self.board.place_white_circle(2,1,True)
        self.board.place_magnet_pos(2,3,False)
        self.board.place_empty_cell(1,0,False)
        self.board.place_empty_cell(2,0,False)
        self.board.place_empty_cell(1,4,False)
        self.board.place_empty_cell(1,5,False)
        self.board.place_empty_cell(2,4,False)
        self.board.place_empty_cell(2,5,False)


        Type(self.board)

class Level14:
    
    def __init__(self):
        self.board = Board(rows=4, cols=4,attempts=2)
        self.board.place_iron(0, 3,False)
        self.board.place_iron(2, 0,False)
        self.board.place_iron(3, 0,False)
        self.board.place_white_circle(1,0,True)
        self.board.place_white_circle(1,2,True)
        self.board.place_white_circle(2,1,True)
        self.board.place_white_circle(2,2,True)
        self.board.place_magnet_pos(3,3,False)



        Type(self.board)

class Level15:
    
    def __init__(self):
        self.board = Board(rows=3, cols=5,attempts=2)
        self.board.place_iron(0, 1,False)
        self.board.place_iron(0, 3,False)
        self.board.place_white_circle(0,0,True)
        self.board.place_white_circle(0,2,True)
        self.board.place_white_circle(1,4,True)
        self.board.place_white_circle(2,4,True)
        self.board.place_magnet_neg(1,2,False)
        self.board.place_magnet_pos(2,2,False)

        Type(self.board)

class Level16:
    
    def __init__(self):
        self.board = Board(rows=5, cols=5,attempts=3)
        self.board.place_iron(1, 2,False)
        self.board.place_iron(3, 2,False)
        self.board.place_white_circle(0,3,True)
        self.board.place_white_circle(0,4,True)
        self.board.place_white_circle(4,0,True)
        self.board.place_white_circle(4,3,True)
        self.board.place_magnet_neg(2,4,False)
        self.board.place_magnet_pos(2,0,False)

        Type(self.board)

class Level17:
    
    def __init__(self):
        self.board = Board(rows=4, cols=4,attempts=2)
        self.board.place_iron(0, 2,False)
        self.board.place_iron(2, 0,False)
        self.board.place_white_circle(1,1,True)
        self.board.place_white_circle(1,3,True)
        self.board.place_white_circle(2,2,True)
        self.board.place_white_circle(3,1,True)
        self.board.place_magnet_neg(3,3,False)
        self.board.place_magnet_pos(0,0,False)
        Type(self.board)

class Level18:
    
    def __init__(self):
        self.board = Board(rows=5, cols=6,attempts=2)
        self.board.place_iron(0, 3,False)
        self.board.place_iron(2, 0,False)
        self.board.place_iron(2, 5,True)

        self.board.place_white_circle(1,3,True)
        self.board.place_white_circle(2,1,True)
        self.board.place_white_circle(2,2,True)
        self.board.place_white_circle(2,3,True)
        self.board.place_magnet_neg(4,3,False)
        self.board.place_magnet_pos(4,2,False)
        self.board.place_empty_cell(0,0,False)
        self.board.place_empty_cell(0,1,False)
        self.board.place_empty_cell(1,0,False)
        self.board.place_empty_cell(1,1,False)
        self.board.place_empty_cell(0,4,False)
        self.board.place_empty_cell(0,5,False)
        self.board.place_empty_cell(1,4,False)
        self.board.place_empty_cell(1,5,False)
        self.board.place_empty_cell(4,0,False)
        self.board.place_empty_cell(4,1,False)
        self.board.place_empty_cell(4,4,False)
        self.board.place_empty_cell(4,5,False)

        Type(self.board)

class Level19:
    
    def __init__(self):
        self.board = Board(rows=5, cols=5,attempts=4)
        self.board.place_iron(0, 1,False)
        self.board.place_iron(0, 3,False)
        self.board.place_iron(4, 1,False)
        self.board.place_iron(4, 3,False)


        self.board.place_white_circle(1,0,True)
        self.board.place_white_circle(1,4,True)
        self.board.place_white_circle(2,1,True)
        self.board.place_white_circle(3,0,True)
        self.board.place_white_circle(3,2,True)
        self.board.place_white_circle(3,4,True)

        self.board.place_magnet_neg(0,2,False)
        self.board.place_magnet_pos(2,2,False)
        self.board.place_empty_cell(0,0,False)
        self.board.place_empty_cell(0,4,False)
        self.board.place_empty_cell(2,0,False)
        self.board.place_empty_cell(2,4,False)
        self.board.place_empty_cell(4,0,False)
        self.board.place_empty_cell(4,4,False)
        

        Type(self.board)

class Level20:
    
    def __init__(self):
        self.board = Board(rows=5, cols=4,attempts=2)
        self.board.place_iron(0, 1,True)
        self.board.place_iron(0, 2,False)
        self.board.place_iron(4, 0,False)


        self.board.place_white_circle(0,3,True)
        self.board.place_white_circle(1,0,True)
        self.board.place_white_circle(2,0,True)
        self.board.place_white_circle(3,0,True)

        self.board.place_magnet_neg(4,2,False)
        self.board.place_magnet_pos(4,3,False)
        

        Type(self.board)

class Level21:
    
    def __init__(self):
        self.board = Board(rows=3, cols=4,attempts=2)
        self.board.place_iron(0, 1,False)
        self.board.place_iron(1, 0,True)
        self.board.place_iron(1, 1,True)
        self.board.place_iron(1, 2,False)

        self.board.place_white_circle(0,2,True)
        self.board.place_white_circle(1,0,True)
        self.board.place_white_circle(2,1,True)

        self.board.place_magnet_neg(2,0,True)
        self.board.place_magnet_pos(2,3,False)
        

        Type(self.board)

class Level22:
    
    def __init__(self):
        self.board = Board(rows=4, cols=5,attempts=3)
        self.board.place_iron(0, 3,True)
        self.board.place_iron(0, 4,False)
        self.board.place_iron(3, 0,False)

        self.board.place_white_circle(0,1,True)
        self.board.place_white_circle(1,0,True)
        self.board.place_white_circle(2,1,True)
        self.board.place_white_circle(1,4,True)

        self.board.place_magnet_pos(3,2,False)
        self.board.place_magnet_neg(0,0,False)

        
        self.board.place_empty_cell(0,2,False)
        self.board.place_empty_cell(1,2,False)
        self.board.place_empty_cell(3,4,False)



        Type(self.board)

class Level23:
    
    def __init__(self):
        self.board = Board(rows=4, cols=5,attempts=3)
        self.board.place_iron(0, 3,False)
        self.board.place_iron(1, 4,True)
        self.board.place_iron(2, 0,False)

        self.board.place_white_circle(0,2,True)
        self.board.place_white_circle(2,1,True)
        self.board.place_white_circle(2,2,True)
        self.board.place_white_circle(2,3,True)

        self.board.place_magnet_pos(3,2,True)
        self.board.place_magnet_neg(3,4,False)

        Type(self.board)

class Level24:
    
    def __init__(self):
        self.board = Board(rows=5, cols=5,attempts=3)
        self.board.place_iron(0, 1,False)
        self.board.place_iron(1, 3,False)
        self.board.place_iron(3, 4,False)

        self.board.place_white_circle(0,3,True)
        self.board.place_white_circle(2,1,True)
        self.board.place_white_circle(2,3,True)
        self.board.place_white_circle(4,1,True)
        self.board.place_white_circle(4,2,True)


        self.board.place_magnet_pos(3,0,False)
        self.board.place_magnet_neg(1,4,False)

        self.board.place_empty_cell(4,0,False)
        self.board.place_empty_cell(4,4,False)

        Type(self.board)

class Level25:
    
    def __init__(self):
        self.board = Board(rows=5, cols=4,attempts=3)
        self.board.place_iron(0, 0,True)
        self.board.place_iron(1, 2,False)
        self.board.place_iron(3, 2,False)
        self.board.place_iron(4, 3,False)


        self.board.place_white_circle(0,3,True)
        self.board.place_white_circle(2,0,True)
        self.board.place_white_circle(4,1,True)
        self.board.place_white_circle(4,2,True)


        self.board.place_magnet_pos(0,3,True)
        self.board.place_magnet_neg(4,0,True)

        Type(self.board)

        