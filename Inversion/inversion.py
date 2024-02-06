from population import *
import random


class Inversion:
    #__slots__ = "probability"

    def __init__(self, probability: float):
        self.probability = probability

    def inversion(self, population: Population, individual_amount_no_elitism: int):
        chromosome_length = Chromosome.size - 1
        for i in range(0, individual_amount_no_elitism):
            chance_inversion = round(random.uniform(0, 1), 2)
            if 0 <= chance_inversion <= self.probability:
                for j in range(0, population.variables_amount):
                    self.reverse_genes(population.individuals[i].chromosome[j].gene, chromosome_length)
            elif self.probability < chance_inversion <= 1:
                continue

    def reverse_genes(self, gene_array: list, chromosome_length):
        start_index = random.randint(0, chromosome_length)
        end_index = random.randint(0, chromosome_length)
        while start_index == end_index:
            end_index = random.randint(0, chromosome_length)

        if start_index > end_index:
            start_index, end_index = end_index, start_index

        gene_array[start_index:end_index + 1] = reversed(gene_array[start_index:end_index + 1])
