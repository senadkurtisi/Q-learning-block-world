from world import BlockWorld
import numpy as np

if __name__ == "__main__":
    world = BlockWorld()
    pos = world.get_starting_position()
    actions = ['north', 'south', 'east', 'west']

    R = 0
    for i in range(500 ):
        action = np.random.randint(4)
        pos = world.try_perform(pos[0], pos[1], actions[action])

        r_current, is_terminal = world.get_reward(pos[0], pos[1])
        R += r_current
        if is_terminal:
            break

    print(R)
