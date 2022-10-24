import random
from random import randint
import EvoSim.globals as g
import EvoSim.environment

genus_count = 0
org_count = 1


def get_current_environment():
    return "EXAMPLE"


def generate_characteristics():
    characteristics = []
    for i in range(0, 10):
        c_valid = False
        while c_valid is False:
            c = randint(0, len(g.characteristics_list) - 1)
            if g.characteristics_list[c] not in characteristics:
                characteristics.append(g.characteristics_list[c])
                c_valid = True
    return characteristics


def reset_genus_count():
    global genus_count
    genus_count = 0


def random_organism():
    return Organism(g.latin_numbers[random.randint(0, len(g.latin_numbers) - 1)])


class Organism(object):
    def __init__(self, genus=None, species=None, characteristics=None, population=None, location=None, ancestors=None, descendants=None):
        global org_count
        self.id = org_count
        org_count += 1

        if ancestors is None:
            self.ancestors = []
        else:
            self.ancestors = ancestors

        if descendants is None:
            self.descendants = []
        else:
            self.descendants = descendants

        if characteristics is None:
            self.characteristics = generate_characteristics()

        self.genetic_code = self.generate_genetic_code()

        if population is None:
            self.population = random.randint(1000, 10000)
        else:
            self.population = population

        if location is None:
            self.location = get_current_environment()
        else:
            self.location = location

        if genus is None and species is None:
            generated_name = self.generate_name()
            self.genus = generated_name[0]
            self.species = generated_name[1]
        elif species is None:
            self.genus = genus
            self.species = g.latin_numbers[random.randint(0, len(g.latin_numbers) - 1)]
        else:
            self.genus = genus
            self.species = species

    def __str__(self):
        return str(self.id) + " " + self.genus + " " + self.species + " " + str(self.characteristics) + " " + self.genetic_code + " " + str(self.population)

    def __repr__(self):
        return str(self.genus) + " " + str(self.species)

    def generate_name(self):
        if len(self.ancestors) == 0:
            global genus_count
            genus_count += 1
            return g.latin_numbers[genus_count - 1], latin_numbers[0]
        else:
            return self.ancestors[0].genus, g.latin_numbers[len(self.ancestors)]

    def generate_genetic_code(self):
        genetic_code = ""
        for c in self.characteristics:
            genetic_code += (c[0] + c[c.find('-') + 1] + "-")
        return genetic_code

    def migrate(self, environment):
        self.location = environment

    def make_extinct(self):
        self.population = 0

    def random_evolve(self):
        genetic_code = list(self.genetic_code)

        target_valid = False
        while not target_valid:
            target = randint(0, len(genetic_code) - 1)
            if genetic_code[target] == '-':
                target = randint(0, len(genetic_code) - 1)
            else:
                genetic_code[target] = g.alphabet[randint(0, 25)]
                self.genetic_code = "".join(genetic_code)
                target_valid = True

    def speciate(self):
        new_org = Organism(ancestors=[self] + self.descendants)
        # print(str([self] + self.ancestors))
        self.descendants = self.descendants + [new_org]
        return new_org

    def create_similar(self):
        return True
