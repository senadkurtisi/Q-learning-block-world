import numpy as np


class BlockWorld:
    def __init__(self, main_p=0.8):
        self.board = np.array([[' ', ' ', ' ', 'N'], [' ', '*', ' ', 'P'], ['S', ' ', ' ', ' ']])
        self.N, self.M = self.board.shape

        self.step_row = {'north': -1, 'south': 1, 'east': 0, 'west': 0}
        self.step_col = {'north': 0, 'south': 0, 'east': +1, 'west': -1}

        self.p_actions = {'north': ['east', 'west'],
                          'south': ['east', 'west'],
                          'east': ['north', 'south'],
                          'west': ['north', 'south']}
        self.main_p = main_p
        self.other_p = (1-self.main_p)/2

    def get_actions(self, row, col):
        if self.board[row, col] in ['S', 'T']:
            return ['END']
        else:
            return ['north', 'south', 'east', 'west']

    def execute_stochastic(self, row, col, action):
        p = np.random.uniform()
        if p <= self.main_p:
            return row + self.step_row[action], col + self.step_col[action]
        elif p <= (self.main_p + self.other_p):
            return row + self.step_row[self.p_actions[action][0]], col + self.step_col[self.p_actions[action][0]]
        else:
            return row + self.step_row[self.p_actions[action][1]], col + self.step_col[self.p_actions[action][1]]

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

        return self.execute_stochastic(row, col, action)

    def get_starting_position(self):
        r, c = np.where(self.board == 'S')
        r, c = r[0], c[0]
        return r, c
