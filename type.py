from cell import Cell

class Magnet_Pos(Cell):
    def __init__(self, position_x, position_y, white_space = False):
        super().__init__(cell_type='R', white_space = white_space)
        self.position_x = position_x
        self.position_y = position_y

class Magnet_Neg(Cell):
    def __init__(self, position_x, position_y, white_space = False):
        super().__init__(cell_type='N', white_space = white_space)
        self.position_x = position_x
        self.position_y = position_y

class Iron(Cell):
    def __init__(self, position_x, position_y, white_space = False):
        super().__init__(cell_type='I', white_space = white_space)
        self.position_x = position_x
        self.position_y = position_y

class White_Circle(Cell):
    def __init__(self, position_x, position_y,white_space = True):
        super().__init__(cell_type='.', white_space = white_space)
        self.position_x = position_x
        self.position_y = position_y

class Empty(Cell):
    def __init__(self, position_x, position_y, white_space = False):
        super().__init__(cell_type=' ', white_space = white_space)
        self.position_x = position_x
        self.position_y = position_y
