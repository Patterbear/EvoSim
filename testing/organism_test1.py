from EvoSim.organism import *


def test():
    organisms = []

    for i in range(0, 9):
        org = Organism()
        organisms.append(org)
        for j in range(0, 8):
            organisms.append(org.speciate())

    for i in range(0, len(organisms) - 1):
        print(organisms[i])

    #print(organisms[0].speciate())