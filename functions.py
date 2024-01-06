from population import *

import math


def chromosome_length(range_start: float, range_end: float, precision_point: int) -> int:
    return math.ceil((math.log((range_end - range_start) * 10 ** precision_point, 2)) + math.log(1, 2))


def chromosome_decode(range_start: float, range_end: float, chromosome: Chromosome) -> int:
    gene = ''.join(map(str, chromosome.gene))
    print(gene, end='\n')
    gene_int = int(gene, 2)
    return range_start + gene_int * (range_end - range_start) / (2 ** chromosome.size - 1)


def population_init(individuals_amount: int, range_start: float, range_end: float) -> Population:
    population = Population(individuals_amount)
    for i in range(0, population.individual_amount):
        our_chromosome = Chromosome()
        actual_value = chromosome_decode(range_start, range_end, our_chromosome)
        our_chromosome.set_actual_value_x(actual_value)
        our_chromosome.set_actual_value_y(fitness_function(our_chromosome.actual_value_x))
        population.individuals[i].add_chromosome(our_chromosome)

    return population


def population_create(individuals_amount: int, old_individuals: list,
                      range_start: float, range_end: float) -> Population:
    population = Population(individuals_amount)
    for i in range(0, len(old_individuals)):
        our_chromosome = Chromosome.only_add_gen(old_individuals[i])
        actual_value = chromosome_decode(range_start, range_end, our_chromosome)
        our_chromosome.set_actual_value_x(actual_value)
        our_chromosome.set_actual_value_y(fitness_function(our_chromosome.actual_value_x))
        population.individuals[i].add_chromosome(our_chromosome)

    return population


def fitness_function(x: float) -> float:
    return x ** 3 - 4 * x ** 2 + x - 4