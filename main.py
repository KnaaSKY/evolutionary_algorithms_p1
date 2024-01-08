from functions import *
from Selection.selection import *
from Crossover.crossover import *


def evolutionary_algorithm(a, b, power_number_intervals, individual_amount, individuals_best_amount,\
                            selection_type, mutation_type, cross_type):
    Chromosome.size = chromosome_length(a, b, power_number_intervals)
    population = population_init(individual_amount, a, b)

    for i in range(0, individual_amount):
        print()
        population.individuals[i].display()

    selekcja = Selection(selection_type, True, 10)
    old_gen = selekcja.selection(population)

    if old_gen is not None:  # Check if old_gen is not None before proceeding
        print()
        print()
        print()

        population = population_create(individual_amount, old_gen, a, b)
        crossover = Crossover(cross_type, individuals_best_amount)
        wynik = crossover.crossover(population, a, b)
        for i, individual in enumerate(wynik.individuals):
            print(f"Individual {i + 1}:")
            print(f"Lancuch genowy: {individual.chromosome.gene}")
            print(f"Wartosc x: {individual.chromosome.actual_value_x}")
            print(f"Wartosc y: {individual.chromosome.actual_value_y}")
            print("\n")
    else:
        print("Error: The selection did not return a valid old_gen.")

    print("DANYLO")

