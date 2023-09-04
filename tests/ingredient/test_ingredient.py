from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient_name = "frango"
    different_ingredient_name = "carne"
    instance = Ingredient(ingredient_name)
    different_instance = Ingredient(different_ingredient_name)
    assert instance.__hash__() == hash(ingredient_name)
    assert instance.__hash__() != hash(different_instance)
    assert instance.name == ingredient_name
    assert instance.name != different_ingredient_name
    assert instance != different_instance
    assert instance == instance
    assert instance.__repr__() == f"Ingredient('{instance.name}')"
    assert instance.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }
