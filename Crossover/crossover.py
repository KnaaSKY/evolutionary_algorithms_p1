from population import *
from functions import *
import copy


class Crossover:
    crossover_type_one_point = 1
    crossover_type_two_point = 2
    crossover_type_homogeneous = 3

    def __init__(self, crossover_type: int, probability: float, individual_amount: int, individual_elitism_amount: int):
        self.crossover_type = crossover_type
        self.individual_amount = individual_amount
        self.individuals_amount_create = individual_amount - individual_elitism_amount
        self.probability = probability

    def crossover(self, individuals_list: list[Individual]):
        # population_gen = []
        #
        # for j in range(self.individuals_best_amount):
        #     individual = population.individuals[j]
        #     if individual is not None and individual.chromosome is not None:
        #         population_gen.append(individual.chromosome.gene)
        #
        # num_remaining_individuals = len(population.individuals) - self.individuals_best_amount
        # while num_remaining_individuals > 0:
        #     chance_crossover = round(random.uniform(0, 1), 2)
        #
        #     if 0 <= chance_crossover <= self.crossover_probability:
        #         match self.crossover_type:
        #             case Crossover.crossover_type_one_point:
        #                 self.crossover_type_one_point_method(population, population_gen)
        #                 num_remaining_individuals -= 1
        #             case Crossover.crossover_type_two_point:
        #                 self.crossover_type_two_point_method(population, population_gen)
        #                 num_remaining_individuals -= 1
        #             case Crossover.crossover_type_homogeneous:
        #                 self.crossover_type_homogeneous_method(population, population_gen)
        #                 num_remaining_individuals -= 1
        #
        #
        # return population

        match self.crossover_type:
            case Crossover.crossover_type_one_point:
                population = self.crossover_type_one_point_method(individuals_list)
                return population
            case Crossover.crossover_type_two_point:
                self.crossover_type_two_point_method(individuals_list)
                num_remaining_individuals -= 1
            case Crossover.crossover_type_homogeneous:
                self.crossover_type_homogeneous_method(individuals_list)
                num_remaining_individuals -= 1

    def crossover_type_one_point_method(self, individuals_list: list[Individual]):
        chromosomes_amount = len(individuals_list[0].chromosome)  # ilosc chromosomow

        population = Population(self.individual_amount, chromosomes_amount)

        chromosome_length = Chromosome.size

        while self.individuals_amount_create > 0:
            chance_crossover = round(random.uniform(0, 1), 2)
            if 0 <= chance_crossover <= self.probability:
                index1, index2 = random.sample(range(len(individuals_list)), 2)
                new_individual1 = Individual()
                for i in range(0, chromosomes_amount):
                    crossover_index = random.randint(0, chromosome_length - 1)
                    new_gene = individuals_list[index1].chromosome[i].gene[:crossover_index] + individuals_list[index2].chromosome[i].gene[crossover_index:]
                    new_chromosome = Chromosome()
                    new_chromosome.set_gene(new_gene)
                    new_individual1.add_chromosome(new_chromosome)
                population.add_individual(new_individual1)
                self.individuals_amount_create -= 1

                if self.individuals_amount_create != 0:
                    new_individual2 = Individual()
                    for i in range(0, chromosomes_amount):
                        crossover_index = random.randint(0, chromosome_length - 1)
                        new_gene = individuals_list[index2].chromosome[i].gene[:crossover_index] + individuals_list[index1].chromosome[i].gene[crossover_index:]
                        new_chromosome = Chromosome()
                        new_chromosome.set_gene(new_gene)
                        new_individual2.add_chromosome(new_chromosome)
                    population.add_individual(new_individual2)
                    self.individuals_amount_create -= 1
            elif self.probability < chance_crossover <= 1:
                continue

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
