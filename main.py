from functions import *
from Selection.selection import *

a: float = -10
b: float = 10
power_number_intervals: int = 6  # 10^power_number_intervals - number of intervals to divide our range
individual_amount: int = 10
individuals_best_amount: int = 5
epochs_amount: int = 0
Chromosome.size = chromosome_length(a, b, power_number_intervals)

population = population_init(individual_amount, a, b)


for i in range(0, individual_amount):
    print()
    population.individuals[i].display()

selekcja = Selection(1, True, individuals_best_amount)


old_gen = selekcja.selection(population)

print()
print()
print()

population = population_create(individual_amount, old_gen, a, b)
for i in range(0, individuals_best_amount):
    print()
    population.individuals[i].display()


print("DANYLO")

