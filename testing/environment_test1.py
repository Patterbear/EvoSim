from EvoSim.environment import *

# Environment Test 1
# Generates a random terrain type and outputs it


def run(envs):
    for i in range(0, envs - 1):
        print(generate_terrain_types())
