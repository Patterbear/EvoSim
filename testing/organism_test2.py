from EvoSim.organism import *


def run():
    reset_genus_count()
    org = Organism()
    org_s1 = org.speciate()
    org_s2 = org.speciate()
    org_s3 = org.speciate()

    new_organisms = [org.ancestors, org_s1.ancestors, org_s2.ancestors, org_s3.ancestors]

    print(new_organisms)