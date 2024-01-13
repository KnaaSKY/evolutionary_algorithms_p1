from population import *

import math


def chromosome_length(range_start: float, range_end: float, precision_point: int) -> int:
    return math.ceil((math.log((range_end - range_start) * 10 ** precision_point, 2)) + math.log(1, 2))


def population_init(individual_amount: int, variables_amount: int) -> Population:
    population = Population(individual_amount, variables_amount)
    for i in range(0, population.individual_amount):
        our_individual = Individual()
        for j in range(0, population.variables_amount):
            our_chromosome = Chromosome()
            our_chromosome.create_gene()
            our_individual.add_chromosome(our_chromosome)
        our_individual.set_fitness_function()
        population.add_individual(our_individual)

    return population

