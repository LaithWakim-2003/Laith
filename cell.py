class Cell:
    def __init__(self,cell_type = '.' , white_space = False):     
        self.cell_type = cell_type
        self.white_space = white_space
    def __str__(self):
        return self.cell_type if self.cell_type != '.' else '.'
