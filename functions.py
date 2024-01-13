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

    # for i in range(0, population.individual_amount):
    #     our_chromosome = Chromosome()
    #     our_chromosome.create_gene()
    #     actual_value = chromosome_decode(range_start, range_end, our_chromosome)
    #     our_chromosome.set_actual_value_x(actual_value)
    #     our_chromosome.set_actual_value_y(fitness_function(our_chromosome.actual_value_x))
    #     population.individuals[i].add_chromosome(our_chromosome)

    return population


# def population_create(individuals_amount: int, old_individuals: dict,
#                       range_start: float, range_end: float) -> Population:
#     population = Population(individuals_amount)
#     keys = list(old_individuals.keys())
#     values = list(old_individuals.values())
#     for i in range(0, len(old_individuals)):
#         our_chromosome = Chromosome()
#         our_chromosome.set_gene(list(keys[i]))
#         our_chromosome.set_actual_value_y(values[i])
#         our_chromosome.set_actual_value_x(chromosome_decode(range_start, range_end, our_chromosome))
#         population.individuals[i].add_chromosome(our_chromosome)
#
#     return population


def calculate_gene_values(population: Population, range_start: float, range_end: float):
    for i in range(population.individual_amount):
        actual_value = chromosome_decode(range_start, range_end, population.individuals[i].chromosome)
        population.individuals[i].chromosome.set_actual_value_x(actual_value)
        population.individuals[i].chromosome.set_actual_value_y(fitness_function(population.individuals[i].chromosome.actual_value_x))

