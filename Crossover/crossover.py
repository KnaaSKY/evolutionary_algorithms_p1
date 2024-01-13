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
                population = self.crossover_type_two_point_method(individuals_list)
                return population
            case Crossover.crossover_type_homogeneous:
                population = self.crossover_type_homogeneous_method(individuals_list)
                return population

    def crossover_type_one_point_method(self, individuals_list: list[Individual]):
        chromosomes_amount = len(individuals_list[0].chromosome)  # ilosc chromosomow

        population = Population(self.individual_amount, chromosomes_amount)

        chromosome_length = Chromosome.size - 1

        while self.individuals_amount_create > 0:
            chance_crossover = round(random.uniform(0, 1), 2)
            if 0 <= chance_crossover <= self.probability:
                index1, index2 = random.sample(range(len(individuals_list)), 2)
                new_individual1 = Individual()
                crossover_index = random.randint(0, chromosome_length)
                for i in range(0, chromosomes_amount):
                    new_gene = individuals_list[index1].chromosome[i].gene[:crossover_index] + individuals_list[index2].chromosome[i].gene[crossover_index:]
                    new_chromosome = Chromosome()
                    new_chromosome.set_gene(new_gene)
                    new_individual1.add_chromosome(new_chromosome)
                population.add_individual(new_individual1)
                self.individuals_amount_create -= 1

                if self.individuals_amount_create != 0:
                    new_individual2 = Individual()
                    for i in range(0, chromosomes_amount):
                        new_gene = individuals_list[index2].chromosome[i].gene[:crossover_index] + individuals_list[index1].chromosome[i].gene[crossover_index:]
                        new_chromosome = Chromosome()
                        new_chromosome.set_gene(new_gene)
                        new_individual2.add_chromosome(new_chromosome)
                    population.add_individual(new_individual2)
                    self.individuals_amount_create -= 1
            elif self.probability < chance_crossover <= 1:
                continue

        return population

    def crossover_type_two_point_method(self, individuals_list: list[Individual]):
        chromosomes_amount = len(individuals_list[0].chromosome)  # ilosc chromosomow

        population = Population(self.individual_amount, chromosomes_amount)

        chromosome_length = Chromosome.size - 1

        while self.individuals_amount_create > 0:
            chance_crossover = round(random.uniform(0, 1), 2)
            if 0 <= chance_crossover <= self.probability:
                index1, index2 = random.sample(range(len(individuals_list)), 2)
                new_individual1 = Individual()

                crossover_index1 = random.randint(0, chromosome_length)
                crossover_index2 = random.randint(0, chromosome_length)
                while crossover_index1 == crossover_index2:
                    crossover_index2 = random.randint(0, chromosome_length)
                if crossover_index1 > crossover_index2:
                    crossover_index1, crossover_index2 = crossover_index2, crossover_index1
                print(f"index1: {index1}, index2: {index2}\ncrossover_index1: {crossover_index1}, crossover_index2: {crossover_index2}")
                for i in range(0, chromosomes_amount):
                    new_gene = individuals_list[index1].chromosome[i].gene[:crossover_index1] + \
                               individuals_list[index2].chromosome[i].gene[crossover_index1:crossover_index2] + \
                               individuals_list[index1].chromosome[i].gene[crossover_index2:]
                    new_chromosome = Chromosome()
                    new_chromosome.set_gene(new_gene)
                    new_individual1.add_chromosome(new_chromosome)
                population.add_individual(new_individual1)
                self.individuals_amount_create -= 1

                if self.individuals_amount_create != 0:
                    new_individual2 = Individual()
                    for i in range(0, chromosomes_amount):
                        new_gene = individuals_list[index2].chromosome[i].gene[:crossover_index1] + \
                                   individuals_list[index1].chromosome[i].gene[crossover_index1:crossover_index2] + \
                                   individuals_list[index2].chromosome[i].gene[crossover_index2:]
                        new_chromosome = Chromosome()
                        new_chromosome.set_gene(new_gene)
                        new_individual2.add_chromosome(new_chromosome)
                    population.add_individual(new_individual2)
                    self.individuals_amount_create -= 1
            elif self.probability < chance_crossover <= 1:
                continue

        return population

    def crossover_type_homogeneous_method(self, individuals_list: list[Individual]):
        chromosomes_amount = len(individuals_list[0].chromosome)  # ilosc chromosomow

        population = Population(self.individual_amount, chromosomes_amount)

        chromosome_length = Chromosome.size

        while self.individuals_amount_create > 0:
            chance_crossover = round(random.uniform(0, 1), 2)
            if 0 <= chance_crossover <= self.probability:
                index1, index2 = random.sample(range(len(individuals_list)), 2)
                new_individual1 = Individual()
                for i in range(0, chromosomes_amount):
                    new_gene = [individuals_list[index1].chromosome[i].gene[j] if j % 2 == 0 else individuals_list[index2][j] for j in range(chromosome_length)]
                    new_chromosome = Chromosome()
                    new_chromosome.set_gene(new_gene)
                    new_individual1.add_chromosome(new_chromosome)
                population.add_individual(new_individual1)
                self.individuals_amount_create -= 1

                if self.individuals_amount_create != 0:
                    new_individual2 = Individual()
                    for i in range(0, chromosomes_amount):
                        new_gene = [individuals_list[index2].chromosome[i].gene[j] if j % 2 == 0 else individuals_list[index1][j] for j in range(chromosome_length)]
                        new_chromosome = Chromosome()
                        new_chromosome.set_gene(new_gene)
                        new_individual2.add_chromosome(new_chromosome)
                    population.add_individual(new_individual2)
                    self.individuals_amount_create -= 1
            elif self.probability < chance_crossover <= 1:
                continue

        return population

