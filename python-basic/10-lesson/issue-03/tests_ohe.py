"""Tests fot OHE"""

import unittest
from one_hot_encoder import fit_transform


class TestFitTransform(unittest.TestCase):
    """
    Test class for fit_transform method
    """

    def test_fit_transform(self):
        """
        Test method with different input data
        """
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        exp_transformed_cities = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        transformed_cities = fit_transform(cities)
        self.assertEqual(
            transformed_cities, exp_transformed_cities
        )

        fruits = ['apple', 'banana', 'orange', 'banana', 'apple']
        exp_transformed_fruits = [
            ('apple', [0, 0, 1]),
            ('banana', [0, 1, 0]),
            ('orange', [1, 0, 0]),
            ('banana', [0, 1, 0]),
            ('apple', [0, 0, 1]),
        ]
        transformed_fruits = fit_transform(fruits)
        self.assertEqual(
            transformed_fruits, exp_transformed_fruits
        )

        animals = ['dog', 'cat', 'mouse', 'dog', 'cat', 'elephant']
        exp_transformed_animals = [
            ('dog', [0, 0, 0, 1]),
            ('cat', [0, 0, 1, 0]),
            ('mouse', [0, 1, 0, 0]),
            ('dog', [0, 0, 0, 1]),
            ('cat', [0, 0, 1, 0]),
            ('elephant', [1, 0, 0, 0]),
        ]
        transformed_animals = fit_transform(animals)
        self.assertEqual(
            transformed_animals, exp_transformed_animals
        )

        numbers = [1, 2, 3, 4]
        exp_transformed_numbers = [
            (1, [0, 0, 0, 1]),
            (2, [0, 0, 1, 0]),
            (3, [0, 1, 0, 0]),
            (4, [1, 0, 0, 0]),
        ]
        transformed_numbers = fit_transform(numbers)
        self.assertEqual(
            transformed_numbers, exp_transformed_numbers
        )

    def test_fit_transform_raises_error(self):
        """
        Test raises TyptError
        """
        with self.assertRaises(TypeError):
            fit_transform()


if __name__ == '__main__':
    unittest.main()
