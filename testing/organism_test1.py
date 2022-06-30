from EvoSim.organism import *


def run():
    reset_genus_count()
    organisms = []

    for i in range(0, 10):
        org = Organism()
        organisms.append(org)
        for j in range(0, 9):
            organisms.append(org.speciate())

    for i in range(0, len(organisms)):
        print(organisms[i])