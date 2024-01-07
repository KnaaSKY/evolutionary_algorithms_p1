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

    def selection(self, population: Population) -> dict:
        population_gen = []
        population_y = []
        for i in range(population.individual_amount):
            population_y.append(population.individuals[i].chromosome.actual_value_y)

        for j in range(population.individual_amount):
            population_gen.append(population.individuals[j].chromosome.gene)

        pop_dict = dict()
        for k in range(population.individual_amount):
            pop_dict[tuple(population_gen[k])] = population_y[k]

        match self.selection_type:
            case Selection.selection_type_best:
                old_gens = self.selection_best_method(pop_dict)
                # for element in old_gens:
                #     print(element, end='\n')
                return old_gens
            case Selection.selection_type_roulette:
                print("selection_type_roulette")
            case Selection.selection_type_tournament:
                print("selection_type_tournament")

    def selection_best_method(self, pop_dict: dict) -> dict:

        if self.min_method == Selection.evaluation_min:
            pop_dict_sorted = dict(sorted(pop_dict.items(), key=lambda item: item[1]))
            # for key, value in pop_dict_sorted.items():
            #     print(f"{key}: {value}")
            best_gen = {}
            for key, value in pop_dict_sorted.items():
                best_gen[key] = value
                if len(best_gen) == self.individuals_best_amount:
                    break
            # for element in best_gen:
            #     print(element, end='\n')
            return best_gen
        else:
            pop_dict_sorted = dict(sorted(pop_dict.items(), key=lambda item: item[1], reverse=True))
            # for key, value in pop_dict_sorted.items():
            #     print(f"{key}: {value}")
            best_gen = {}
            for key, value in pop_dict_sorted.items():
                best_gen[key] = value
                if len(best_gen) == self.individuals_best_amount:
                    break
            # for element in best_gen:
            #     print(element, end='\n')
            return best_gen


    def selection_roulette_method(self):
        pass

    def selection_tournament_method(self):
        pass