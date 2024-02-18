from functions import *
from Selection.selection import *
from Crossover.crossover import *
from Inversion.inversion import *
from Mutation.mutation import *
import matplotlib.pyplot as p
import time
import statistics


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
                           crossover_probability, mutation_probability, inversion_probability, minimisation, func_type):
    individual_amount_no_elitism = individual_amount - individual_elitism_amount
    Chromosome.size = chromosome_length(a, b, power_number_intervals)
    Individual.range_start = a
    Individual.range_end = b

    start_time = time.time()
    selection = Selection(selection_type, minimisation, individual_selection_amount)
    crossover = Crossover(crossover_type, crossover_probability, individual_amount, individual_elitism_amount, func_type)
    inversion = Inversion(inversion_probability)
    mutation = Mutation(mutation_type, mutation_probability)

    population = population_init(individual_amount, variable_amount, func_type)
    the_best_individuals = {}
    x = []
    y = []
    average = []
    standard_deviation = []
    with open('result.txt', 'w') as file:
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
            x.append(i)
            y.append(best_individuals[0].fitness_function_value)
            suma: float = 0.0
            values_list = []
            for k in range(0, individual_amount):
                values_list.append(population.individuals[k].fitness_function_value)
                suma = sum(values_list)
            average.append(suma / individual_amount)
            standard_deviation.append(statistics.stdev(values_list))

    for key, value in the_best_individuals.items():
        print(key)
        value.display()

    timee = time.time() - start_time
    p.plot(x, y)
    p.title("Wykres wartości funkcji")
    p.xlabel("Iteracja")
    p.ylabel("Wartość funkcji")
    p.savefig('wykres1.png')
    p.show()
    p.plot(x, average)
    p.title("Wykres średniej wartości funkcji")
    p.xlabel("Iteracja")
    p.ylabel("Średnia wartość funkcji")
    p.savefig('wykres2.png')
    p.show()
    p.plot(x, standard_deviation)
    p.title("Wykres odchylenia standardowego")
    p.xlabel("Iteracja")
    p.ylabel("Odchylenie standardowe")
    p.savefig('wykres3.png')
    p.show()
    p.close()
    print("DANYLO")
    # print("--- %s seconds ---" % (time.time() - start_time))

    print("DANYLO")
   # print("--- %s seconds ---" % (time.time() - start_time))

    return the_best_individuals, timee
