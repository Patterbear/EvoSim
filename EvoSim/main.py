from EvoSim.organism import Organism


def main():

    org1 = Organism()
    org2 = Organism()
    # print(org1)
    # print(org2)

    initial_code = org2.genetic_code

    for i in range(0, 20):
        org2.random_evolve()

    print(initial_code + "\n" + org2.genetic_code)


if __name__ == "__main__":

    main()
