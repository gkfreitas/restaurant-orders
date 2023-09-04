from src.models.dish import Dish
from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501
import pytest


# Req 2
def test_dish():
    ingredient_instace = Ingredient("frango")
    dish_name = "yakissoba"
    different_dish_name = "strogonoff"
    different_dish_price = 99
    different_instance = Dish(different_dish_name, different_dish_price)
    dish_price = 50.00
    instance = Dish(dish_name, dish_price)
    instance.add_ingredient_dependency(ingredient_instace, 1)
    print(instance.get_ingredients())
    assert instance.name == dish_name
    assert instance.__hash__() == hash(instance.__repr__())
    assert instance.__hash__() != hash(1)
    assert instance == Dish(dish_name, dish_price)
    assert instance != different_instance
    assert (
        instance.__repr__()
        == f"Dish('{instance.name}', R${instance.price:.2f})"
    )
    with pytest.raises(TypeError):
        Dish("a", "a")
    with pytest.raises(ValueError):
        Dish("AA", -1)
    assert instance.recipe.get(ingredient_instace) == 1
    assert instance.get_restrictions() == {
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
    }
    assert instance.get_ingredients() == {ingredient_instace}
