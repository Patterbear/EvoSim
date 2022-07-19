from EvoSim.organism import Organism
from testing import organism_test1, organism_test2, organism_test3


def main():

    org1 = Organism()
    org2 = Organism(ancestors=[org1])

    org3 = Organism()
    print(org1)
    print(org2)
    print(org3)

    initial_code = org2.genetic_code

    for i in range(0, 20):
        org2.random_evolve()

    print(initial_code + "\n" + org2.genetic_code)


if __name__ == "__main__":
    organism_test1.run()
    organism_test2.run()
    organism_test3.run()

    # main()
