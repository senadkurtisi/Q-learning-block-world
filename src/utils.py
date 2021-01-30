from IPython.display import display, Math
import matplotlib.pyplot as plt

action_map = {
    '-1': r'End',
    '0': r'\uparrow',
    '1': r'\downarrow',
    '2': r'\rightarrow',
    '3': r'\leftarrow'
}

def visualize_optimal_actions(optimal_actions):
    """ Creates a visualization of optimal actions
        per iteration for each state. Actions are
        displayed as TeX arrows indicating {north, south, east, west}
        or End.
    """
    assert isinstance(optimal_actions, dict), "Optimal actions must be a dictionary!"

    for state, actions in optimal_actions.items():
        optimal_act = f"{state}"

        for i, action in enumerate(actions):
            optimal_act += f"| {action_map[str(action)]}"
        
        display(Math(optimal_act))


def show_v_values_dual(v_values_1, v_values_2, it_1, it_2):
    """ Displays V-values graphs for each state for
        received as result of two different algorithms.
    
    Arguments:
        v_values_1: V-values result of algorithm 1
        v_values_2: V-values result of algorithm 2
        it_1: number of iterations/episodes after which
              algorithm 1 has converged
        it_2: number of iterations/episodes after which
              algorithm 2 has converged
    """
    v_iter = [value[-1] for value in v_values_1.values()]

    fig, axs = plt.subplots(6, 2, figsize=(15, 18))
    axs[5, 1].remove()
    for i, (k, v) in enumerate(v_values_2.items()):
        if i < 6:
            col = 0
        else:
            col = 1

        row = i % 6
        axs[row, col].plot(v, label="Q learning", zorder=0)
        axs[row, col].hlines(v_iter[i], 0, it_2,
                             colors='orange',
                             label="Q iteration",
                             zorder=5)
        axs[row, col].set_ylabel(f"State: {k}")
        axs[row, col].legend()

    fig.suptitle("V values for each state")
    plt.show()


def show_v_values_single(v_values):
    """ Displays V-values graphs for each state.
    """
    fig, axs = plt.subplots(6, 2, figsize=(15, 18))
    axs[5, 1].remove()
    for i, (k, v) in enumerate(v_values.items()):
        if i < 6:
            col = 0
        else:
            col = 1

        row = i % 6
        axs[row, col].plot(v)
        axs[row, col].set_ylabel(f"State: {k}")
        
    fig.suptitle("V values for each state")
    plt.show()

