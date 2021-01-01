from world import BlockWorld
import numpy as np

if __name__ == "__main__":
    world = BlockWorld()
    pos = world.get_starting_position()
    actions = ['north', 'south', 'east', 'west']
    world.initialize_q_values()
    for k, v in world.q_values.items():
        print(k, v)
