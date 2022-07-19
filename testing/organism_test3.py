from EvoSim.organism import *

# Organism Test 3
# Creates 5 descendants from an organism and prints its list of descendants


def run():
    org = Organism()
    for i in range(0, 4):
        org.speciate()
    print(org.descendants)