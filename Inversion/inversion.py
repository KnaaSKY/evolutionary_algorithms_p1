from population import *
import random


class Inversion:
    def __init__(self, probability: float):
        self.probability = probability

    def inversion(self, population: Population):
        chromosome_length = population.individuals[0].chromosome.size
        for i in range(population.individual_amount):
            chance_inversion = round(random.uniform(0, 1), 2)
            if 0 <= chance_inversion <= self.probability:
                print(population.individuals[i].chromosome.actual_value_x, end='==')
                print(i, end='..')
                self.reverse_genes(population.individuals[i].chromosome.gene, chromosome_length)
            elif self.probability < chance_inversion <= 1:
                continue

    def reverse_genes(self, gene_array: list, chromosome_length):
        length: int = chromosome_length - 1
        start_index = random.randint(0, length)
        end_index = random.randint(0, length)
        while start_index == end_index:
            start_index = random.randint(0, length)
            end_index = random.randint(0, length)

        if start_index > end_index:
            start_index, end_index = end_index, start_index

        print(start_index, end='**')
        print(end_index, end='\n')

        gene_array[start_index:end_index + 1] = reversed(gene_array[start_index:end_index + 1])
