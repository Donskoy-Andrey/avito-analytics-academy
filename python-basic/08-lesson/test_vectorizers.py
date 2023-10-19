"""
Unittests for vectorizers
"""

import unittest
from base import CountVectorizerError
from vectorizers import CountVectorizer


class TestCountVectorizer(unittest.TestCase):
    """
    Test for CountVectorizer class.
    """

    def setUp(self):
        self.vectorizer = CountVectorizer()
        self.corpus = [
            "Crock Pot Pasta Never boil pasta again",
            "Pasta Pomodoro Fresh ingredients Parmesan to taste"
        ]
        self.count_matrix = [
            [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
        ]
        self.names = [
            'crock', 'pot', 'pasta', 'never', 'boil', 'again',
            'pomodoro', 'fresh', 'ingredients', 'parmesan', 'to', 'taste'
        ]

    def test_fit_transform(self):
        """
        Test fit_transform method

        :raise AssertionError:
            Incorrect behaviour
        """
        count_matrix = self.vectorizer.fit_transform(self.corpus)
        self.assertEqual(
            count_matrix, self.count_matrix
        )

    def test_get_feature_names(self):
        """
        Test get_feature_names method

        :raise AssertionError:
            Incorrect behaviour
        """
        self.vectorizer.fit_transform(self.corpus)
        names = self.vectorizer.get_feature_names()
        self.assertEqual(
            names, self.names
        )

    def test_get_feature_names_exception(self):
        """
        Test get_feature_names method

        :raise AssertionError:
            Incorrect behaviour
        """
        self.assertRaises(
            CountVectorizerError,
            self.vectorizer.get_feature_names
        )


if __name__ == "__main__":
    unittest.main()
