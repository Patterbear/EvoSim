import random

from EvoSim.globals import terrain_types, terrain_descriptors
import EvoSim.organism as o

env_count = 0

# TEST ENV TYPES
env_types = ['g', 'w', 's', 'r']


def generate_terrain_types():
    terrains = []
    for i in range(0, 5):
        terrains.append([terrain_descriptors[
                             random.randint(0, len(terrain_descriptors) - 1)],
                         terrain_types[random.randint(0, len(terrain_types) - 1)]])
    return terrains


def populate_environment():
    # organisms = [Organism(), random_organism()]
    organisms = [o.Organism(), o.random_organism()]
    print(organisms[1])
    return organisms


class Environment(object):
    def __init__(self, terrains=None, organisms=None, size=None, grid=None):
        global env_count
        env_count = env_count + 1

        self.id = env_count

        if terrains is None:
            self.terrains = generate_terrain_types()
        else:
            self.terrains = terrains

        if organisms is None:
            self.organisms = populate_environment()
            print(self.organisms)

        if grid is None:
            new_grid = []
            for i in range(0, 39):
                inner_grid = []
                for j in range(0, 39):
                    inner_grid.append(0)
                new_grid.append(inner_grid)
            #print(new_grid)
            self.grid = new_grid

    def print_grid(self):
        for i in range(0, len(self.grid)-1):
            print(self.grid[i])

    def test_grid_fill(self):
        for i in range(0, len(self.grid)-1):
            for j in range(0, len(self.grid[i])):
                self.grid[i][j] = random.choice(env_types)
