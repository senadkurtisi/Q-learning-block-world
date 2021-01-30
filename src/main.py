from world import BlockWorld
from q_learning import *
import matplotlib.pyplot as plt

MAX_ITER = 5000
MAX_EPISODES = 100000
import time

if __name__ == "__main__":
    # world = BlockWorld(0.8)
    # it_1, v_values_1, optimal_actions_1 = q_value_iterative(world, 0.9, MAX_ITER)
    # print(it_1)
    world = BlockWorld(0.8)
    t1 = time.time()
    it_2, v_values_2, optimal_actions_2 = q_learning(world, MAX_EPISODES, 0.9, 0.2)
    # print(it_2)
    print(time.time()-t1)
    #
    #
    # v_iter = [value[-1] for value in v_values_1.values()]
    # fig, axs = plt.subplots(6, 2, figsize=(15, 18))
    # axs[5, 1].remove()
    # for i, (k, v) in enumerate(v_values_2.items()):
    #     if i < 6:
    #         col = 0
    #     else:
    #         col = 1
    #
    #     row = i % 6
    #     axs[row, col].plot(v, label="Q learning", zorder=0)
    #     axs[row, col].hlines(v_iter[i], 0, it_2,
    #                          colors='orange',
    #                          label="Q iteration",
    #                          zorder=5)
    #     axs[row, col].set_ylabel(f"State: {k}")
    #     axs[row, col].legend()
    #
    # fig.suptitle("V values for each state")
    # plt.savefig('q_learning_constant.png', bbox_inches='tight')
