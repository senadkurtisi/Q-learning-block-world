
def q_value_iterative(world, gamma=0.9, max_iter=float('inf')):
    iter_ = 0
    converged_states = []
    converged = False

    while iter_ < max_iter and not converged:
        new_q_values = {k: v.copy() for k, v in world.q_values.items()}

        for state in world.q_values.keys():
            pos = tuple(map(int, state[1:-1].split(',')))
            possible_actions = world.get_actions(pos[0], pos[1])

            for action in possible_actions:
                possible_outcomes = [action] + world.p_actions[action]
                new_q_value, is_terminal = world.get_reward(pos[0], pos[1])

                if not is_terminal:
                    for side_action in possible_outcomes:
                        next_row, next_col = world.execute(pos[0], pos[1], side_action)
                        if side_action != action:
                            p = world.other_p
                        else:
                            p = world.main_p

                        best_action_next = world.get_best_action(next_row, next_col)
                        new_q_value += gamma * p * world.q_values[str((next_row, next_col))][best_action_next]

                new_q_value = round(new_q_value, 2)
                new_q_values[str((pos[0], pos[1]))][action] = new_q_value

                if new_q_value == world.q_values[str((pos[0], pos[1]))][action]:
                    conv_ = [pos, action]
                    if conv_ not in converged_states:
                        converged_states.append(conv_)

                    if len(converged_states) == 38:
                        converged = True

        world.q_values = new_q_values
        iter_ += 1

    return iter_
