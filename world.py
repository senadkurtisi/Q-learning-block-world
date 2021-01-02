import numpy as np


class BlockWorld:
    def __init__(self, main_p=0.8):
        self.board = np.array([[' ', ' ', ' ', 'P'], [' ', '*', ' ', 'N'], ['S', ' ', ' ', ' ']])
        self.num_states = 11
        self.N, self.M = self.board.shape

        self.step_row = {'north': -1, 'south': 1, 'east': 0, 'west': 0}
        self.step_col = {'north': 0, 'south': 0, 'east': +1, 'west': -1}

        self.p_actions = {'north': ['east', 'west'],
                          'south': ['east', 'west'],
                          'east': ['north', 'south'],
                          'west': ['north', 'south'],
                          'END': []}
        self.main_p = main_p
        self.other_p = (1-self.main_p)/2

        self.rewards = {'terminal': {'P': 1, 'N': -1},
                        'step': -0.04}

        self.initialize_q_values()

    def get_actions(self, row, col):
        if self.is_terminal(row, col):
            return ['END']
        else:
            return ['north', 'south', 'east', 'west']

    def get_best_action(self, row, col):
        dict_key_pos = str((row, col))
        return max(self.q_values[dict_key_pos], key=self.q_values[dict_key_pos].get)

    def get_reward(self, row, col):
        if self.is_terminal(row, col):
            return self.rewards['terminal'][self.board[row, col]], True
        else:
            return self.rewards['step'], False

    def is_terminal(self, row, col):
        return self.board[row, col] in ['P', 'N']

    def try_perform(self, row, col, action):
        p = np.random.uniform()
        if p <= self.main_p:
            return self.execute(row, col, action)
        elif p <= (self.main_p + self.other_p):
            return self.execute(row, col, self.p_actions[action][0])
        else:
            return self.execute(row, col, self.p_actions[action][1])

    def execute(self, row, col, action=None, stochastic=True):
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

    def get_starting_position(self):
        r, c = np.where(self.board == 'S')
        r, c = r[0], c[0]
        return r, c

    def initialize_q_values(self):
        self.q_values = {}
        for row in range(self.N):
            for col in range(self.M):
                if self.board[row, col] != '*':
                    self.q_values[str((row, col))] = {}
                    actions = self.get_actions(row, col)
                    for action in actions:
                        self.q_values[str((row, col))][action] = 0
