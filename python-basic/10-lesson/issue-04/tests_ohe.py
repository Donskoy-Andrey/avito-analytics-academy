"""Tests fot OHE"""

import pytest
from one_hot_encoder import fit_transform


def test_fit_transform():
    """
    Test method with different input data
    """
    # Test case 1
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    exp_transformed_cities = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    transformed_cities = fit_transform(cities)
    assert transformed_cities == exp_transformed_cities

    # Test case 2
    fruits = ['apple', 'banana', 'orange', 'banana', 'kiwi']
    exp_transformed_fruits = [
        ('apple', [0, 0, 0, 1]),
        ('banana', [0, 0, 1, 0]),
        ('orange', [0, 1, 0, 0]),
        ('banana', [0, 0, 1, 0]),
        ('kiwi', [1, 0, 0, 0]),
    ]
    transformed_fruits = fit_transform(fruits)
    assert transformed_fruits == exp_transformed_fruits

    # Test case 3
    animals = ['dog', 'cat', 'dog', 'bird']
    exp_transformed_animals = [
        ('dog', [0, 0, 1]),
        ('cat', [0, 1, 0]),
        ('dog', [0, 0, 1]),
        ('bird', [1, 0, 0]),
    ]
    transformed_animals = fit_transform(animals)
    assert transformed_animals == exp_transformed_animals

    # Test case 4
    colors = ['red', 'green', 'blue']
    exp_transformed_colors = [
        ('red', [0, 0, 1]),
        ('green', [0, 1, 0]),
        ('blue', [1, 0, 0]),
    ]
    transformed_colors = fit_transform(colors)
    assert transformed_colors == exp_transformed_colors


def test_fit_transform_error():
    """
    Test raises TypeError
    """
    # Test case 5 - exception handling
    with pytest.raises(TypeError):
        fit_transform()
