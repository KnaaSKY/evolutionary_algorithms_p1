from population import *


class Crossover:
    crossover_probability = 0
    crossover_type_one_point = 1
    crossover_type_two_point = 2
    crossover_type_homogeneous = 3
    crossover_type_shuffle = 4

    def __init__(self, crossover_type: int, individuals_best_amount: int):
        self.crossover_type = crossover_type
        self.individuals_best_amount = individuals_best_amount

    def crossover(self, population: Population):
        population_gen = []
        for j in range(self.individuals_best_amount):
            individual = population.individuals[j]
            if individual is not None and individual.chromosome is not None:
                population_gen.append(individual.chromosome.gene)
        match self.crossover_type:
            case Crossover.crossover_type_one_point:
                cross_population = self.crossover_type_one_point_method(population, population_gen)
                return cross_population
            case Crossover.crossover_type_two_point:
                print("crossover_type_two_point")
            case Crossover.crossover_type_homogeneous:
                print("crossover_type_homogeneous")
            case Crossover.crossover_type_shuffle:
                print("crossover_type_shuffle")

    def crossover_type_one_point_method(self, population: Population, population_gen: list):
        new_individuals = []

        for i in range(0, len(population_gen), 2):
            crossover_index = random.randint(0, len(population_gen[i]) - 1)

            # Skrzyżuj geny
            new_gene1 = population_gen[i][:crossover_index] + population_gen[i + 1][crossover_index:]
            new_gene2 = population_gen[i + 1][:crossover_index] + population_gen[i][crossover_index:]

            # Utwórz nowe obiekty Chromosome
            new_chromosome1 = Chromosome()
            new_chromosome1.set_gene(new_gene1)

            new_chromosome2 = Chromosome()
            new_chromosome2.set_gene(new_gene2)

            # Utwórz nowe obiekty Individual i dodaj je do listy
            new_individual1 = Individual()
            new_individual1.add_chromosome(new_chromosome1)
            new_individuals.append(new_individual1)

            new_individual2 = Individual()
            new_individual2.add_chromosome(new_chromosome2)
            new_individuals.append(new_individual2)

        # Zaktualizuj populację nowymi osobnikami
        population.individuals = new_individuals

        return population
