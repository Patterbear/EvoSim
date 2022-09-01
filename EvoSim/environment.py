import random

from globals import terrain_types, terrain_descriptors

env_count = 0


def generate_terrain_types():
    terrains = []
    for i in range(0, 5):
        terrains.append([terrain_descriptors[random.randint(0, len(terrain_descriptors) - 1)], terrain_types[random.randint(0, len(terrain_types) - 1)]])
    return terrains


class Environment(object):
    def __init__(self, terrains=None, organisms=None, size=None):
        global env_count
        env_count = env_count + 1

        self.id = env_count

        if terrains is None:
            self.terrains = generate_terrain_types()

