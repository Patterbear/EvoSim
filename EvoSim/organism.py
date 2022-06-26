import random
from random import randint

org_count = 1
latin_numbers = ["primus", "secundus", "tertius", "quartus", "quintus", "sextus", "septimus", "octavus", "nonus", "decimus"]
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
characteristics_list = [
    "immune-strong",
    "immune-weak",
    "thick-skin",
    "thin-skin",
    "birth-egg",
    "birth-live",
    "reproduce-a",
    "reproduce-s",
    "skin-dark",
    "skin-light",
    "vision-monocular",
    "vision-bimonocular",
    "vision-colour",
    "diet-carnivore",
    "diet-omnivore",
    "diet-herbivore",
    "movement-wings",
    "movement-flight",
    "movement-fast",
    "movement-agile",
    "movement-slow",
    "breathe-underwater",
    "breathe-land",
    "large-ears",
    "medium-ears",
    "small-ears",
    "large-feet",
    "medium-feet",
    "small-feet",
    "large-nose",
    "medium-nose",
    "small-nose",
    "size-large",
    "size-medium",
    "size-small"

]


class Organism(object):
    def __init__(self):
        global org_count
        self.id = org_count
        org_count += 1
        self.name = self.generate_name()
        self.characteristics = self.generate_characteristics()
        self.genetic_code = self.generate_genetic_code()

        self.population = randint(100, 1000)
        self.location = None

    def __str__(self):
        return str(self.id) + " " + self.name + " " + str(self.characteristics) + " " + self.genetic_code + " " + str(self.population)

    def generate_name(self):
        return "Organism " + latin_numbers[self.id - 1]

    def generate_genetic_code(self):
        genetic_code = ""
        for c in self.characteristics:
            genetic_code += (c[0] + c[c.find('-') + 1] + "-")
        return genetic_code

    def migrate(self, environment):
        self.location = environment


    def generate_characteristics(self):
        characteristics = []
        for i in range(0, 10):
            characteristics.append(characteristics_list[randint(0, len(characteristics_list) - 1)])
        return characteristics

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
                genetic_code[target] = alphabet[randint(0, 25)]
                self.genetic_code = "".join(genetic_code)
                target_valid = True

