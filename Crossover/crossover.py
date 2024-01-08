from population import *
from functions import *
import copy
class Crossover:
    crossover_type_one_point = 1
    crossover_type_two_point = 2
    crossover_type_homogeneous = 3


    def __init__(self, crossover_type: int, individuals_best_amount: int, cross_probability: float):
        self.crossover_type = crossover_type
        self.individuals_best_amount = individuals_best_amount
        self.crossover_probability = cross_probability

    def crossover(self, population: Population):
        population_gen = []

        for j in range(self.individuals_best_amount):
            individual = population.individuals[j]
            if individual is not None and individual.chromosome is not None:
                population_gen.append(individual.chromosome.gene)

        num_remaining_individuals = len(population.individuals) - self.individuals_best_amount
        while num_remaining_individuals > 0:
            chance_crossover = round(random.uniform(0, 1), 2)

            if 0 <= chance_crossover <= self.crossover_probability:
                match self.crossover_type:
                    case Crossover.crossover_type_one_point:
                        self.crossover_type_one_point_method(population, population_gen)
                        num_remaining_individuals -= 1
                    case Crossover.crossover_type_two_point:
                        self.crossover_type_two_point_method(population, population_gen)
                        num_remaining_individuals -= 1
                    case Crossover.crossover_type_homogeneous:
                        self.crossover_type_homogeneous_method(population, population_gen)
                        num_remaining_individuals -= 1


        return population

    def crossover_type_one_point_method(self, population: Population, population_gen: list):
        new_individuals = []
        idx1, idx2 = random.sample(range(len(population_gen)), 2)

        crossover_index = random.randint(0, len(population_gen[0]) - 1)

        new_gene1 = population_gen[idx1][:crossover_index] + population_gen[idx2][crossover_index:]
        new_gene2 = population_gen[idx2][:crossover_index] + population_gen[idx1][crossover_index:]

        new_chromosome1 = Chromosome()
        new_chromosome1.set_gene(new_gene1)

        new_chromosome2 = Chromosome()
        new_chromosome2.set_gene(new_gene2)

        new_individual1 = Individual()
        new_individual1.add_chromosome(new_chromosome1)
        new_individuals.append(new_individual1)

        new_individual2 = Individual()
        new_individual2.add_chromosome(new_chromosome2)
        new_individuals.append(new_individual2)



        population_gen.append(new_gene1)
        population_gen.append(new_gene2)

        for i, new_individual in enumerate(new_individuals):
            index_to_update = self.find_next_empty_index(population)

        if index_to_update is not None:

            new_individual_copy = copy.deepcopy(new_individual)

            population.individuals[index_to_update] = new_individual_copy
        return population

    def crossover_type_two_point_method(self, population: Population, population_gen: list):
        new_individuals = []
        idx1, idx2 = random.sample(range(len(population_gen)), 2)

        size = len(population_gen[idx1])

        crossover_index1 = random.randint(0, size - 1)
        crossover_index2 = random.randint(crossover_index1 + 1, size)

        new_gene1 = population_gen[idx1][:crossover_index1] + \
                    population_gen[idx2][crossover_index1:crossover_index2] + \
                    population_gen[idx1][crossover_index2:]

        new_gene2 = population_gen[idx2][:crossover_index1] + \
                    population_gen[idx1][crossover_index1:crossover_index2] + \
                    population_gen[idx2][crossover_index2:]

        new_chromosome1 = Chromosome()
        new_chromosome1.set_gene(new_gene1)

        new_chromosome2 = Chromosome()
        new_chromosome2.set_gene(new_gene2)

        new_individual1 = Individual()
        new_individual1.add_chromosome(new_chromosome1)
        new_individuals.append(new_individual1)

        new_individual2 = Individual()
        new_individual2.add_chromosome(new_chromosome2)
        new_individuals.append(new_individual2)

        population_gen.append(new_gene1)
        population_gen.append(new_gene2)

        for i, new_individual in enumerate(new_individuals):
            index_to_update = self.find_next_empty_index(population)

        if index_to_update is not None:
            new_individual_copy = copy.deepcopy(new_individual)

            population.individuals[index_to_update] = new_individual_copy

        return population

    def crossover_type_homogeneous_method(self, population: Population, population_gen: list):
        new_individuals = []
        idx1, idx2 = random.sample(range(len(population_gen)), 2)

        size = len(population_gen[idx1])

        new_gene1 = [population_gen[idx1][j] if j % 2 == 0 else population_gen[idx2][j] for j in range(size)]
        new_gene2 = [population_gen[idx2][j] if j % 2 == 0 else population_gen[idx1][j] for j in range(size)]

        new_chromosome1 = Chromosome()
        new_chromosome1.set_gene(new_gene1)

        new_chromosome2 = Chromosome()
        new_chromosome2.set_gene(new_gene2)

        new_individual1 = Individual()
        new_individual1.add_chromosome(new_chromosome1)
        new_individuals.append(new_individual1)

        new_individual2 = Individual()
        new_individual2.add_chromosome(new_chromosome2)
        new_individuals.append(new_individual2)

        population_gen.append(new_gene1)
        population_gen.append(new_gene2)

        for i, new_individual in enumerate(new_individuals):
            index_to_update = self.find_next_empty_index(population)

        if index_to_update is not None:
            new_individual_copy = copy.deepcopy(new_individual)

            population.individuals[index_to_update] = new_individual_copy
        return population

    def find_next_empty_index(self, population: Population):
        for i, individual in enumerate(population.individuals[10:]):
            if individual is None:
                return i + 10
            elif individual.chromosome is None or individual.chromosome.gene is None:
                return i + 10

        return None
