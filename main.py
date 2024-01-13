from functions import *
from Selection.selection import *
from Inversion.inversion import *

a: float = -10
b: float = 10
power_number_intervals: int = 6  # 10^power_number_intervals - number of intervals to divide our range
individual_amount: int = 5
variable_amount = 1
individuals_best_amount: int = 3
epochs_amount: int = 0
Chromosome.size = chromosome_length(a, b, power_number_intervals)
Individual.range_start = a
Individual.range_end = b

population = population_init(individual_amount, variable_amount)


for i in range(0, individual_amount):
    print()
    population.individuals[i].display()


selekcja = Selection(1, True, individuals_best_amount)
best_gens = selekcja.selection(population)
for i in range(0, 3):
    for j in range(0, variable_amount):
        print(best_gens[i].chromosome[j].gene, end="    ")
        print(best_gens[i].chromosome_values[j])



# population = population_create(individual_amount, old_gen, a, b)
# for i in range(0, individuals_best_amount):
#     print()
#     population.individuals[i].display()


# inversion = Inversion(0.5)
# inversion.inversion(population)
# calculate_gene_values(population, a, b)
# for i in range(0, individuals_best_amount):
#     print()
#     population.individuals[i].display()



print("DANYLO")


