import numpy as np


class BlockWorld:
    def __init__(self):
        self.board = np.array([[' ', ' ', ' ', 'N'], [' ', '*', ' ', 'P'],
                               ['S', ' ', ' ', ' ']])
        self.N, self.M = self.board.shape

        self.step_row = {'north': -1, 'south': 1, 'east': 0, 'west': 0}
        self.step_col = {'north': 0, 'south': 0, 'east': +1, 'west': -1}

    def get_actions(self, row, col):
        if self.board[row, col] in ['S', 'T']:
            return ['END']
        else:
            return ['north', 'south', 'east', 'west']

    def try_perform(self, row, col, action=None):
        assert action is not None, "No action selected!"

        if action == 'north':
            if (row-1) < 0 or self.board[row-1, col] == '*':
                return row, col
        elif action == 'south':
            if (row+1) >= self.N or self.board[row+1, col] == '*':
                return row, col
        elif action == 'east':
            if (col+1) >= self.M or self.board[row, col+1] == '*':
                return row, col
        elif action == 'west':
            if (col-1) < 0 or self.board[row, col-1] == '*':
                return row, col

        return row + self.step_row[action], col + self.step_col[action]
