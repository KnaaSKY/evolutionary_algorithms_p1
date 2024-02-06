from functions import *
from Selection.selection import *
from Crossover.crossover import *
from Inversion.inversion import *
from Mutation.mutation import *
import time
# a: float = -10
# b: float = 10
# power_number_intervals: int = 6  # 10^power_number_intervals - number of intervals to divide our range
# individual_amount: int = 7
# variable_amount = 1
# individual_selection_amount: int = 3
# individual_elitism_amount = 2
# individual_amount_no_elitism = individual_amount - individual_elitism_amount
# epochs_amount: int = 0
# minimisation = True
# Chromosome.size = chromosome_length(a, b, power_number_intervals)
# Individual.range_start = a
# Individual.range_end = b
a: float = 0.0
b: float = 0.0
power_number_intervals: int = 0  # 10^power_number_intervals - number of intervals to divide our range
individual_amount: int = 0
variable_amount: int = 0
individual_selection_amount: int = 0
individual_elitism_amount: int = 0
epochs_amount: int = 0
minimisation: bool = True
selection_type: int = 0
mutation_type: int = 0
crossover_type: int = 0
crossover_probability: float = 0.0
mutation_probability: float = 0.0
inversion_probability: float = 0.0


def evolutionary_algorithm(variable_amount, a, b, power_number_intervals, individual_amount,
                           individual_selection_amount,
                           individual_elitism_amount, epochs_amount, selection_type, mutation_type, crossover_type,
                           crossover_probability, mutation_probability, inversion_probability, minimisation):
    individual_amount_no_elitism = individual_amount - individual_elitism_amount
    Chromosome.size = chromosome_length(a, b, power_number_intervals)
    Individual.range_start = a
    Individual.range_end = b

    start_time = time.time()
    selection = Selection(selection_type, minimisation, individual_selection_amount)
    crossover = Crossover(crossover_type, crossover_probability, individual_amount, individual_elitism_amount)
    inversion = Inversion(inversion_probability)
    mutation = Mutation(mutation_type, mutation_probability)

    population = population_init(individual_amount, variable_amount)
    the_best_individuals = {}
    for i in range(0, epochs_amount):
        best_individuals = selection.selection(population)
        the_best_individuals[i] = best_individuals[0]
        elitists = [best_individuals[j] for j in range(0, individual_elitism_amount)]
        population = crossover.crossover(best_individuals)
        mutation.mutation(population, individual_amount_no_elitism)
        inversion.inversion(population, individual_amount_no_elitism)
        update_data(population)
        for j in elitists:
            population.add_individual(j)

    for key, value in the_best_individuals.items():
        print(key)
        value.display()

    print("DANYLO")
    print("--- %s seconds ---" % (time.time() - start_time))

    return the_best_individuals, time.time() - start_time
