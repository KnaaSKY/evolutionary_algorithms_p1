from population import *
from functions import *

class Crossover:
    crossover_probability = 0
    crossover_type_one_point = 1
    crossover_type_two_point = 2
    crossover_type_homogeneous = 3


    def __init__(self, crossover_type: int, individuals_best_amount: int):
        self.crossover_type = crossover_type
        self.individuals_best_amount = individuals_best_amount

    def crossover(self, population: Population,a ,b):
        population_gen = []
        for j in range(self.individuals_best_amount):
            individual = population.individuals[j]
            if individual is not None and individual.chromosome is not None:
                population_gen.append(individual.chromosome.gene)
        match self.crossover_type:
            case Crossover.crossover_type_one_point:
                cross_population = self.crossover_type_one_point_method(population, population_gen, a, b)
                return cross_population
            case Crossover.crossover_type_two_point:
                cross_population = self.crossover_type_two_point_method(population, population_gen, a, b)
                return cross_population
            case Crossover.crossover_type_homogeneous:
                cross_population = self.crossover_type_homogeneous_method(population, population_gen, a, b)
                return cross_population


    def crossover_type_one_point_method(self, population: Population, population_gen: list, a, b):
        new_individuals = population.individuals[:10]

        for i in range(0, len(population_gen), 2):
            crossover_index = random.randint(0, len(population_gen[i]) - 1)
            print(crossover_index)

            # Zabezpieczenie przed sytuacją, gdy crossover_index jest równe długości chromosomu
            if crossover_index == len(population_gen[i]):
                crossover_index -= 1

            new_gene1 = population_gen[i][:crossover_index] + population_gen[i + 1][crossover_index:]
            new_gene2 = population_gen[i + 1][:crossover_index] + population_gen[i][crossover_index:]

            new_chromosome1 = Chromosome()
            new_chromosome1.set_gene(new_gene1)
            actual_value = chromosome_decode(a, b, new_chromosome1)
            new_chromosome1.set_actual_value_x(actual_value)
            new_chromosome1.set_actual_value_y(fitness_function(new_chromosome1.actual_value_x))

            new_chromosome2 = Chromosome()
            new_chromosome2.set_gene(new_gene2)
            actual_value = chromosome_decode(a, b, new_chromosome2)
            new_chromosome2.set_actual_value_x(actual_value)
            new_chromosome2.set_actual_value_y(fitness_function(new_chromosome2.actual_value_x))

            new_individual1 = Individual()
            new_individual1.add_chromosome(new_chromosome1)
            new_individuals.append(new_individual1)

            new_individual2 = Individual()
            new_individual2.add_chromosome(new_chromosome2)
            new_individuals.append(new_individual2)

        population.individuals = new_individuals

        return population

    def crossover_type_two_point_method(self, population: Population, population_gen: list, a, b):
        new_individuals = population.individuals[:10]

        for i in range(0, len(population_gen), 2):
            crossover_index1 = random.randint(0, len(population_gen[i]) - 1)
            crossover_index2 = random.randint(crossover_index1 + 1, len(population_gen[i]))

            # Zabezpieczenie przed sytuacją, gdy crossover_index2 jest równe długości chromosomu
            if crossover_index2 == len(population_gen[i]):
                crossover_index2 -= 1

            print(f"Crossover points: {crossover_index1}, {crossover_index2}")

            new_gene1 = population_gen[i][:crossover_index1] + \
                        population_gen[i + 1][crossover_index1:crossover_index2] + \
                        population_gen[i][crossover_index2:]

            new_gene2 = population_gen[i + 1][:crossover_index1] + \
                        population_gen[i][crossover_index1:crossover_index2] + \
                        population_gen[i + 1][crossover_index2:]

            new_chromosome1 = Chromosome()
            new_chromosome1.set_gene(new_gene1)
            actual_value = chromosome_decode(a, b, new_chromosome1)
            new_chromosome1.set_actual_value_x(actual_value)
            new_chromosome1.set_actual_value_y(fitness_function(new_chromosome1.actual_value_x))

            new_chromosome2 = Chromosome()
            new_chromosome2.set_gene(new_gene2)
            actual_value = chromosome_decode(a, b, new_chromosome2)
            new_chromosome2.set_actual_value_x(actual_value)
            new_chromosome2.set_actual_value_y(fitness_function(new_chromosome2.actual_value_x))

            new_individual1 = Individual()
            new_individual1.add_chromosome(new_chromosome1)
            new_individuals.append(new_individual1)

            new_individual2 = Individual()
            new_individual2.add_chromosome(new_chromosome2)
            new_individuals.append(new_individual2)

        population.individuals = new_individuals

        return population

    def crossover_type_homogeneous_method(self, population: Population, population_gen: list, a, b):
        new_individuals = population.individuals[:10]

        for i in range(0, len(population_gen), 2):
            size = len(population_gen[i])


            new_gene1 = [population_gen[i][j] if j % 2 == 0 else population_gen[i + 1][j] for j in range(size)]
            new_gene2 = [population_gen[i + 1][j] if j % 2 == 0 else population_gen[i][j] for j in range(size)]


            new_chromosome1 = Chromosome()
            new_chromosome1.set_gene(new_gene1)
            actual_value = chromosome_decode(a, b, new_chromosome1)
            new_chromosome1.set_actual_value_x(actual_value)
            new_chromosome1.set_actual_value_y(fitness_function(new_chromosome1.actual_value_x))

            new_chromosome2 = Chromosome()
            new_chromosome2.set_gene(new_gene2)
            actual_value = chromosome_decode(a, b, new_chromosome2)
            new_chromosome2.set_actual_value_x(actual_value)
            new_chromosome2.set_actual_value_y(fitness_function(new_chromosome2.actual_value_x))


            new_individual1 = Individual()
            new_individual1.add_chromosome(new_chromosome1)
            new_individuals.append(new_individual1)

            new_individual2 = Individual()
            new_individual2.add_chromosome(new_chromosome2)
            new_individuals.append(new_individual2)


        population.individuals = new_individuals

        return population

