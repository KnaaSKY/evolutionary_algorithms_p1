from population import *


class Selection:
    selection_type_best = 1
    selection_type_roulette = 2
    selection_type_tournament = 3

    evaluation_min = True  # True for finding minimum, False for finding maximum

    def __init__(self, selection_type: int, min_method: bool, individuals_best_amount: int):
        self.selection_type = selection_type
        self.min_method = min_method
        self.individuals_best_amount = individuals_best_amount

    def selection(self, population: Population):
        population_y = []
        for i in range(population.individual_amount):
            population_y.append(population.individuals[i].chromosome.actual_value_y)

        match self.selection_type:
            case Selection.selection_type_best:
                self.selection_best_method(population_y)
            case Selection.selection_type_roulette:
                print("selection_type_roulette")
            case Selection.selection_type_tournament:
                print("selection_type_tournament")

    def selection_best_method(self, population_y: list):
        for element in population_y:
            print(element, end='\n')                        # DO ZROBIENIA
        print()
        print()

        if self.min_method == Selection.evaluation_min:
            population_y.sort()
            for element in population_y:
                print(element, end='\n')
        else:
            population_y.sort(reverse=True)
            for element in population_y:
                print(element, end='\n')


    def selection_roulette_method(self):
        pass

    def selection_tournament_method(self):
        pass