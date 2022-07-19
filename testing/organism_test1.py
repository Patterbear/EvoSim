from EvoSim.organism import *

# Organism Test 1
# Creates 10 organisms and creates 9 for each one.


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