from population import *


class Selection:
    #__slots__ = "selection_type", "min_method", "individuals_best_amount"

    selection_type_best = 1
    selection_type_tournament = 2
    selection_type_roulette = 3

    evaluation_min = True  # True for finding minimum, False for finding maximum

    def __init__(self, selection_type: int, min_method: bool, individuals_best_amount: int):
        self.selection_type = selection_type
        self.min_method = min_method
        self.individuals_best_amount = individuals_best_amount

    def selection(self, population: Population) -> list[Individual]:
        match self.selection_type:
            case Selection.selection_type_best:
                best_chromosomes = self.selection_best_method(population)
                return best_chromosomes
            case Selection.selection_type_tournament:
                best_chromosomes = self.selection_tournament_method(population)
                return best_chromosomes
            case Selection.selection_type_roulette:
                print("selection_type_roulette")

    def selection_best_method(self, population: Population) -> list[Individual]:

        if self.min_method == Selection.evaluation_min:
            individuals_sorted = sorted(population.individuals, key=lambda x: x.fitness_function_value)
            individuals_list = []
            for i in range(0, self.individuals_best_amount):
                individuals_list.append(individuals_sorted[i])
            return individuals_list
        else:
            individuals_sorted = sorted(population.individuals, key=lambda x: x.fitness_function_value, reverse=True)
            individuals_list = []
            for i in range(0, self.individuals_best_amount):
                individuals_list.append(individuals_sorted[i])
            return individuals_list


    def selection_roulette_method(self, population: Population) -> list[Individual]:
        pass

    def selection_tournament_method(self, population: Population) -> list[Individual]:
        tournament_individual_amount = int(population.individual_amount / self.individuals_best_amount)
        tournament_size = len(population.individuals) // tournament_individual_amount
        random.shuffle(population.individuals)
        tournaments = []

        for i in range(0, len(population.individuals), tournament_size):
            sublist = population.individuals[i:i + tournament_size]
            tournaments.append(sublist)

        remainder = len(population.individuals) % tournament_individual_amount
        for i in range(remainder):
            tournaments[i].append(population.individuals.pop())

        if remainder != 0:
            tournaments.pop()

        individuals_list = []
        for tournament in tournaments:
            if self.min_method == Selection.evaluation_min:
                tournament_sorted = sorted(tournament, key=lambda x: x.fitness_function_value)
            else:
                tournament_sorted = sorted(tournament, key=lambda x: x.fitness_function_value, reverse=True)
            individuals_list.append(tournament_sorted[0])

        return individuals_list
