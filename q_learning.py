import numpy as np


def q_value_iterative(world, discount=0.9, max_iter=float('inf')):
    """ Performs Q-value iteration algorithm. """
    optimal_actions = {} # holds optimal actions per iteration for each state
    v_values = {} # holds optimal Q-value for each state per iteration

    for k in world.q_values.keys():
        v_values[k] = []
        optimal_actions[k] = []

    iter_ = 0
    converged_states = []
    converged = False

    while iter_ < max_iter and not converged:
        new_q_values = {k: v.copy() for k, v in world.q_values.items()}

        for state in world.q_values.keys():
            # Transforms dict key to a tuple, example: "(2, 1))" -> (2, 1)
            current_state = tuple(map(int, state[1:-1].split(',')))
            # Which actions can be executed by the agent in the current state
            possible_actions = world.get_actions(current_state[0], current_state[1])

            for action in possible_actions:
                # include actions which would be executed if agent slipped
                possible_outcomes = [action] + world.p_actions[action]
                new_q_value, is_terminal = world.get_reward(current_state[0], current_state[1])

                if not is_terminal:
                    for side_action in possible_outcomes:
                        # What would be the next state?
                        next_row, next_col = world.execute(current_state[0], current_state[1], side_action)
                        if side_action != action: # agent has slipped
                            p = world.other_p
                        else:
                            p = world.main_p

                        best_action_next = world.get_best_action(next_row, next_col)
                        new_q_value += discount * p * world.q_values[str((next_row, next_col))][best_action_next]

                new_q_values[str((current_state[0], current_state[1]))][action] = new_q_value

                if abs(new_q_value - world.q_values[str((current_state[0], current_state[1]))][action]) < 1e-4:
                    conv_ = [current_state, action]
                    if conv_ not in converged_states:
                        converged_states.append(conv_)

                    if len(converged_states) == 38:
                        converged = True

        # Perform synchronous update to Q-values
        world.q_values = new_q_values

        for k, v in world.q_values.items():
            v_values[k].append(max(list(v.values())))
            optimal_actions[k].append(np.argmax(list(v.values())))

        optimal_actions[str((0, 3))][-1] = -1
        optimal_actions[str((1, 3))][-1] = -1

        iter_ += 1

    return iter_, v_values, optimal_actions


def q_learning(world, episodes, discount=0.9, epsilon=0.1, alpha=None):
    """ Performs Q-value iteration algorithm. """
    if alpha is None: # we should use adaptive learning rate
        adaptive = True
    else:
        adaptive = False

    optimal_actions = {} # holds optimal actions per iteration for each state
    v_values = {} # holds optimal Q-value for each state per iteration

    for k in world.q_values.keys():
        v_values[k] = []
        optimal_actions[k] = []

    converged_states = []
    converged = False

    for episode in range(1, episodes+1):
        if converged:
            break

        current_state = world.get_starting_position()
        is_terminal = False

        if adaptive:
            alpha = np.log(episode+1)/(episode+1)
            
        while not is_terminal:
            epsilon_p = np.random.uniform()
            if epsilon_p <= epsilon: 
                # Perform Epsilon-greedy exploration of the environment
                possible_actions = world.get_actions(current_state[0], current_state[1])
                if len(possible_actions) == 1:
                    action = possible_actions[0]
                else:
                    action = np.random.choice(possible_actions)
            else:
                action = world.get_best_action(current_state[0], current_state[1])

            new_q, is_terminal = world.get_reward(current_state[0], current_state[1])
            if not is_terminal:
                # What would be the next state?
                next_pos = world.try_perform(current_state[0], current_state[1], action)
                best_action_next = world.get_best_action(next_pos[0], next_pos[1])
                new_q += discount * world.q_values[str((next_pos[0], next_pos[1]))][best_action_next]

            # Perform the TD-update to Q(current_state, action)
            temporal_difference = new_q - world.q_values[str((current_state[0], current_state[1]))][action]
            td_q = world.q_values[str((current_state[0], current_state[1]))][action] + alpha * temporal_difference

            if abs(td_q-world.q_values[str((current_state[0], current_state[1]))][action]) < 1e-4:
                conv_ = [current_state, action]
                if conv_ not in converged_states:
                    converged_states.append(conv_)

                if len(converged_states) == 38:
                    converged = True

            world.q_values[str((current_state[0], current_state[1]))][action] = td_q

            if not is_terminal:
                current_state = next_pos

        for k, v in world.q_values.items():
            v_values[k].append(max(list(v.values())))
            optimal_actions[k].append(np.argmax(list(v.values())))

        optimal_actions[str((0, 3))][-1] = -1
        optimal_actions[str((1, 3))][-1] = -1

    return episode, v_values, optimal_actions
