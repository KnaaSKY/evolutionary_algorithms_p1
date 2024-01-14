from functions import *
from Selection.selection import *
from Crossover.crossover import *
from Inversion.inversion import *
from Mutation.mutation import *

a: float = -10
b: float = 10
power_number_intervals: int = 6  # 10^power_number_intervals - number of intervals to divide our range
individual_amount: int = 7
variable_amount = 1
individual_selection_amount: int = 3
individual_elitism_amount = 2
individual_amount_no_elitism = individual_amount - individual_elitism_amount
epochs_amount: int = 0
Chromosome.size = chromosome_length(a, b, power_number_intervals)
Individual.range_start = a
Individual.range_end = b

population = population_init(individual_amount, variable_amount)

for i in range(0, individual_amount):
    print()
    population.individuals[i].display()

selekcja = Selection(1, True, individual_selection_amount)
best_gens = selekcja.selection(population)
for i in range(0, 3):
    for j in range(0, variable_amount):
        print(best_gens[i].chromosome[j].gene, end="    ")
        print(best_gens[i].chromosome_values[j])

crossover = Crossover(2, 0.7, individual_amount, individual_elitism_amount)
population = crossover.crossover(best_gens)

for i in range(0, individual_amount_no_elitism):
    for j in range(0, variable_amount):
        print(population.individuals[i].chromosome[j].gene, end="\n")


mutation = Mutation(1, 0.3)
mutation.mutation(population, individual_amount_no_elitism)
for i in range(0, individual_amount_no_elitism):
    for j in range(0, variable_amount):
        print(population.individuals[i].chromosome[j].gene, end="\n")

# inversion = Inversion(0.7)
# inversion.inversion(population, individual_amount_no_elitism)
# for i in range(0, individual_amount_no_elitism):
#     print()
#     population.individuals[i].display()
#
# for i in range(0, individual_amount_no_elitism):
#     print()
#     population.individuals[i].display()
print("DANYLO")
