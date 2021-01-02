from world import BlockWorld
from q_learning import q_value_iterative
import time

MAX_ITER = 5000

if __name__ == "__main__":
    world = BlockWorld(0.8)
    t1 = time.time()
    print(q_value_iterative(world, 0.9, MAX_ITER))
    print(time.time()-t1)
    
    for k, v in world.q_values.items():
        print(k, v)
