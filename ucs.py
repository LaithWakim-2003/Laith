from heapq import heappush, heappop
from collections import deque
from colorama import Back, Fore
from availablemoves import AvailableMoves
import copy

from movement import Movement

class UCS:
    def __init__(self):
        self.my_grids = []
        self.visited = set()
        
    def setterboard(self, board):
        self.my_grids.append(board)
        self.ucs(board)

    def visited_checker(self, board):
        serialized_board = self.serialize_board(board)
        return serialized_board in self.visited

    def serialize_board(self, board):
        serialized_board = ""
        for row in board.lm_grid:
            for cell in row:
                serialized_board += cell.cell_type
            serialized_board += "\n"
        return serialized_board

    def ucs(self, start_board):
        queue = []
        start_state = BoardState(start_board, 0)
        heappush(queue, start_state)

        while queue:
            current_state = heappop(queue)
            cost  = current_state.cost
            board = current_state.board
            if self.visited_checker(board):
                continue
            elif not self.visited_checker(board):
                print("NOT VISITED")
                self.print_board(board)
                
            if self.win_condition(board):
                print("WINNER BOARD")
                print(f"Total cost to reach this state: {cost}")
                self.print_board(board)
                return True

            self.visited.add(self.serialize_board(board))
            
            magnets_positions = self.find_magnets_positions(board)
            if not magnets_positions:
                print("No magnet found on this board.")
                continue

            for magnet_x, magnet_y in magnets_positions:
                my_available_moves_list = self.check_available_moves(magnet_x, magnet_y, board)

                for move in my_available_moves_list:
                    new_board = self.create_new_board(board, move)
                    new_cost = cost + 1
                    new_state = BoardState(new_board, new_cost)
                    heappush(queue, new_state)

        print("No solution found.")
        return False

    def find_magnets_positions(self, board):
        magnets_positions = []
        for x in range(board.rows):
            for y in range(board.cols):
                if board.lm_grid[x][y].cell_type in ['R', 'N']:
                    magnets_positions.append((x, y))
        return magnets_positions

    def check_available_moves(self, magnet_x, magnet_y, board):
        my_available_moves_list = []
        for x in range(board.rows):
            for y in range(board.cols):
                if board.lm_grid[x][y].cell_type == '.':
                    available_moves = AvailableMoves(
                        magnet_x = magnet_x,
                        magnet_y = magnet_y,
                        available_x = x,
                        available_y = y
                    )
                    my_available_moves_list.append(available_moves)
        return my_available_moves_list

    def create_new_board(self, board, move):
        from board import Board
        new_board = Board(board.rows, board.cols)
        for row in range(board.rows):
            for col in range(board.cols):
                new_board.lm_grid[row][col] = copy.deepcopy(board.lm_grid[row][col])
        self.move_magnet(new_board, move.magnet_x, move.magnet_y, move.available_x, move.available_y)
        return new_board

    def move_magnet(self, new_board, input_x, input_y, new_input_x, new_input_y):
        if new_board.lm_grid[input_x][input_y].cell_type in ['R']:
            if new_board.lm_grid[new_input_x][new_input_y].white_space:
                Movement().place_magnet_pos(new_board, new_input_x, new_input_y, True)
            else:
                Movement().place_magnet_pos(new_board, new_input_x, new_input_y, False)
            Movement().move_cells_to_magnet(new_board, new_input_x, new_input_y, new_board.rows, new_board.cols)
        elif new_board.lm_grid[input_x][input_y].cell_type in ['N']:
            if new_board.lm_grid[new_input_x][new_input_y].white_space:
                Movement().place_magnet_neg(new_board, new_input_x, new_input_y, True)
            else:
                Movement().place_magnet_neg(new_board, new_input_x, new_input_y, False)
            Movement().move_cells_away_from_magnet(new_board, new_input_x, new_input_y, new_board.rows, new_board.cols)

        if new_board.lm_grid[input_x][input_y].white_space:
            Movement().place_normal_cell(new_board, input_x, input_y, True)
        else:
            Movement().place_normal_cell(new_board, input_x, input_y, False)

    def print_board(self, new_board):
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

    def win_condition(self, board):
        winner = True
        for row in range(board.rows):
            for col in range(board.cols):
                if board.lm_grid[row][col].white_space == True:
                    if board.lm_grid[row][col].cell_type in ['I', 'N', 'R']:
                        pass
                    else:
                        winner = False
                else:
                    continue
        return winner

class BoardState:
    def __init__(self, board, cost):
        self.board = board
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost
