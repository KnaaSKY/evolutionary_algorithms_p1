from population import *
import random


class Mutation:
    mutation_type_one_point = 1
    mutation_type_two_points = 2
    mutation_type_edge = 3

    def __init__(self, mutation_type: int, probability: float):
        self.mutation_type = mutation_type
        self.probability = probability

    def mutation(self, population: Population, individual_amount_no_elitism: int):

        match self.mutation_type:
            case Mutation.mutation_type_one_point:
                self.mutation_one_point_method(population, individual_amount_no_elitism)
            case Mutation.mutation_type_two_points:
                self.mutation_two_points_method(population, individual_amount_no_elitism)
            case Mutation.mutation_type_edge:
                self.mutation_edge_method(population, individual_amount_no_elitism)

    def mutation_one_point_method(self, population: Population, individual_amount_no_elitism: int):
        length = population.individuals[0].chromosome[0].size
        for i in range(individual_amount_no_elitism):
            chance_mutation = round(random.uniform(0, 1), 2)
            if 0 <= chance_mutation <= self.probability:
                index_change = random.randint(0, length - 1)
                print(f"gen: {i} index: {index_change}")
                for j in range(population.variables_amount):
                    population.individuals[i].chromosome[j].gene[index_change] = 0 if (
                        population.individuals[i].chromosome[j].gene[index_change] == 1) else 1

    def mutation_two_points_method(self, population: Population, individual_amount_no_elitism: int):
        length = population.individuals[0].chromosome[0].size
        for i in range(individual_amount_no_elitism):
            chance_mutation = round(random.uniform(0, 1), 2)
            if 0 <= chance_mutation <= self.probability:
                index_change = random.randint(0, length - 1)
                index2_change = random.randint(0, length - 1)
                while index_change == index2_change:
                    index2_change = random.randint(0, length - 1)
                print(f"gen: {i} index1: {index_change} index2: {index2_change}")
                for j in range(population.variables_amount):
                    population.individuals[i].chromosome[j].gene[index_change] = 0 if (
                            population.individuals[i].chromosome[j].gene[index_change] == 1) else 1
                    population.individuals[i].chromosome[j].gene[index2_change] = 0 if (
                            population.individuals[i].chromosome[j].gene[index2_change] == 1) else 1

    def mutation_edge_method(self, population: Population, individual_amount_no_elitism: int):
        length = population.individuals[0].chromosome[0].size
        for i in range(individual_amount_no_elitism):
            chance_mutation = round(random.uniform(0, 1), 2)
            if 0 <= chance_mutation <= self.probability:
                index_change = random.choice([0, length-1])
                print(f"gen: {i} index: {index_change}")
                for j in range(population.variables_amount):
                    population.individuals[i].chromosome[j].gene[index_change] = 0 if (
                            population.individuals[i].chromosome[j].gene[index_change] == 1) else 1
