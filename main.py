import math
import random
import secrets


class Population:

    def __init__(self, amount_of_individuals):
        self.individual_amount = amount_of_individuals
        self.individuals = []
        for i in range(0, amount_of_individuals + 1):
            new_individual = Individual()
            self.individuals.append(new_individual)


class Individual:

    def __init__(self):
        self.chromosome = None

    def add_chromosome(self, new_chromosome):
        self.chromosome = new_chromosome

    def display(self):
        # print(f"Rozmiar chromosoma: {self.chromosome.size}")
        print(f"Lancuch genowy: {self.chromosome.gene}")
        print(f"Wartosc rzeczywista: {self.chromosome.actual_value}")


class Chromosome:
    size = 0

    def __init__(self):
        # self.gene = [0,0,0,0,1,1,0,0,1,0,0,1,0,0,1,0,0,1,0,1,1,0,1,0]
        self.gene = []
        self.actual_value = 0
        for i in range(0, self.size):
            number = random.choice([0, 1])
            self.gene.append(number)

    # def display(self):
    #     print(f"Rozmiar: {self.size}")
    #     print(f"Lancuch genowy: {self.gene}")
    #     print(f"Wartosc rzeczywista: {self.actual_value}")

    def set_actual_value(self, value):
        self.actual_value = value


def chromosome_length(range_start, range_end, precision_point):
    return math.ceil((math.log((range_end - range_start) * 10 ** precision_point, 2)) + math.log(1, 2))


def chromosome_decode(range_start, range_end, chromosome):
    gene = ''.join(map(str, chromosome.gene))
    gene_int = int(gene, 2)
    return range_start + gene_int * (range_end - range_start) / (2 ** chromosome.size - 1)


def population_init(individual_amount):
    population = Population(individual_amount)
    for i in range(0, population.individual_amount):
        our_chromosome = Chromosome()
        actual_value = chromosome_decode(a, b, our_chromosome)
        our_chromosome.set_actual_value(actual_value)
        population.individuals[i].add_chromosome(our_chromosome)

    return population


a = -10
b = 10
precision = 6
individual_amount = 5
epochs_amount = 0
Chromosome.size = chromosome_size = chromosome_length(a, b, precision)


populacja = population_init(individual_amount)


for i in range(0, individual_amount):
    print()
    populacja.individuals[i].display()

print("DANYLO")
