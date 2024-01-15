import random
import benchmark_functions as bf


class Chromosome:
    size = None

    def __init__(self):
        # self.gene = [0,0,0,0,1,1,0,0,1,0,0,1,0,0,1,0,0,1,0,1,1,0,1,0]
        self.gene = []
        self.gene_decoded = 0

    def create_gene(self):
        for i in range(0, self.size):
            number = random.choice([0, 1])
            self.gene.append(number)
        self.update_gene()

    def set_gene(self, new_gene: list):
        self.gene = new_gene
        # self.update_gene()

    def update_gene(self):
        gene_temp = ''.join(map(str, self.gene))
        self.gene_decoded = int(gene_temp, 2)


class Individual:
    range_start = None
    range_end = None

    def __init__(self):
        self.chromosome = []  # [Chromosome1, Chromosome2]
        self.chromosome_values = []  # [value1, value2]
        self.fitness_function_value = None

    def add_chromosome(self, new_chromosome: Chromosome):
        self.chromosome.append(new_chromosome)
        # value = self.chromosome_decode(Individual.range_start, Individual.range_end, new_chromosome)
        # self.chromosome_values.append(value)

    def update_values(self):
        for chromosome in self.chromosome:
            value = self.chromosome_decode(Individual.range_start, Individual.range_end, chromosome)
            self.chromosome_values.append(value)
        self.set_fitness_function()

    def set_fitness_function(self):
        self.fitness_function_value = self.fitness_function(self.chromosome_values)

    @staticmethod
    def fitness_function(variables: list) -> float:  # variables = [variable1, variable2, variable3]
        variables_amount = len(variables)
        func = bf.DeJong3()
        match variables_amount:
            case 1:
                return variables[0] ** 3 - 7 * variables[0] ** 2 + -10 * variables[0] - 4
            case 2:
                # return variables[0] ** 3 * variables[1] ** 3 - 2 * variables[0] ** 2
                return func(variables)

    @staticmethod
    def chromosome_decode(range_start: float, range_end: float, chromosome: Chromosome) -> int:
        return range_start + chromosome.gene_decoded * (range_end - range_start) / (2 ** chromosome.size - 1)

    def display(self):
        for i in range(0, len(self.chromosome)):
            print(self.chromosome[i].gene, end="    ")
            print(self.chromosome_values[i])
        print(f"Wartosc fitness_function: {self.fitness_function_value}")


class Population:

    def __init__(self, individual_amount: int, variables_amount: int):
        self.individual_amount: int = individual_amount
        self.individuals = []
        self.variables_amount = variables_amount

    def add_individual(self, new_individual: Individual):
        self.individuals.append(new_individual)


