import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        arqv = open(source_path)
        self.file = csv.reader(arqv, delimiter=",")
        self.dishes = set()
        self.run_instances()

    def run_instances(self):
        first = 0
        for row in self.file:
            if first == 0:
                first += 1
            else:
                dish_instance = Dish(row[0], float(row[1]))
                self.dishes.add(dish_instance)
                for dish in self.dishes:
                    if dish.name == row[0]:
                        ingredient_instance = Ingredient(row[2])
                        dish.add_ingredient_dependency(
                            ingredient_instance, int(row[3])
                        )
