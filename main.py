from functions import *
from Selection.selection import *
from Crossover.crossover import *


def evolutionary_algorithm(a, b, power_number_intervals, individual_amount,individuals_best_amount):
    Chromosome.size = chromosome_length(a, b, power_number_intervals)
    population = population_init(individual_amount, a, b)

    for i in range(0, individual_amount):
        print()
        population.individuals[i].display()

    selekcja = Selection(1, True, 10)
    old_gen = selekcja.selection(population)



    print()
    print()
    print()

    population = population_create(individual_amount, old_gen, a, b)
    crossover = Crossover(1, individuals_best_amount)
    wynik = crossover.crossover(population)
    for i, individual in enumerate(wynik.individuals):
        print(f"Individual {i + 1}:")
        print(f"Lancuch genowy: {individual.chromosome.gene}")
        print(f"Wartosc x: {individual.chromosome.actual_value_x}")
        print(f"Wartosc y: {individual.chromosome.actual_value_y}")
        print("\n")
    #for i in range(0, individuals_best_amount):
      #  print()
       # population.individuals[i].display()

    print("DANYLO")

# Pozostała część kodu, która korzysta z funkcji evolutionary_algorithm, zostaje bez zmian

