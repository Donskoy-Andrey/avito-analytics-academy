"""
Unittests for vectorizers
"""

import unittest
import numpy as np
from base import CountVectorizerError, BaseTestClass
from vectorizers import CountVectorizer, TfIdfTransformer, TfIdfVectorizer


class TestCountVectorizer(unittest.TestCase, BaseTestClass):
    """
    Test for `CountVectorizer` class.
    """

    def setUp(self):
        self.vectorizer = CountVectorizer()

    def test_fit_transform(self):
        """
        Test `fit_transform` method

        :raise AssertionError:
            Incorrect behaviour
        """
        count_matrix = self.vectorizer.fit_transform(self.corpus)
        self.assertEqual(
            count_matrix, self.count_matrix
        )

    def test_get_feature_names(self):
        """
        Test `get_feature_names` method

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
        Test `get_feature_names` method

        :raise AssertionError:
            Incorrect behaviour
        """
        self.assertRaises(
            CountVectorizerError,
            self.vectorizer.get_feature_names
        )


class TestTfIdfTransformer(unittest.TestCase, BaseTestClass):
    """
    Test for `TfIdfTransformer` class.
    """

    def setUp(self):
        self.transformer = TfIdfTransformer()
        self.vectorizer = CountVectorizer()

    def test_tf_transform(self):
        """
        Test `tf_transform` method

        :raise AssertionError:
            Incorrect behaviour
        """
        count_matrix = self.vectorizer.fit_transform(self.corpus)
        term_frequency = self.transformer.tf_transform(count_matrix)

        self.assertEqual(
            np.isclose(np.array(term_frequency), self.term_frequency).all(),
            True
        )

    def test_idf_transform(self):
        """
        Test `idf_transform` method

        :raise AssertionError:
            Incorrect behaviour
        """
        count_matrix = self.vectorizer.fit_transform(self.corpus)
        inverse_df = self.transformer.idf_transform(count_matrix)
        self.assertEqual(
            np.isclose(np.array(inverse_df), self.inverse_df).all(),
            True
        )

    def test_tf_idf(self):
        """
        Test `tf_idf` method

        :raise AssertionError:
            Incorrect behaviour
        """
        count_matrix = self.vectorizer.fit_transform(self.corpus)
        term_frequency = self.transformer.tf_transform(count_matrix)
        inverse_df = self.transformer.idf_transform(count_matrix)
        tf_idf = self.transformer.tf_idf(term_frequency, inverse_df)
        self.assertEqual(
            np.isclose(np.array(tf_idf), self.tf_idf).all(),
            True
        )


class TestTfIdfVectorizer(unittest.TestCase, BaseTestClass):
    """
    Test for `TfIdfVectorizer` class.
    """

    def setUp(self):
        self.vectorizer = TfIdfVectorizer()

    def test_fit_transform(self):
        """
        Test `fit_transform` method

        :raise AssertionError:
            Incorrect behaviour
        """
        tf_idf_matrix = self.vectorizer.fit_transform(self.corpus)
        self.assertEqual(
            np.isclose(np.array(tf_idf_matrix), self.tf_idf).all(),
            True
        )

    def test_get_feature_names(self):
        """
        Test `get_feature_names` method

        :raise AssertionError:
            Incorrect behaviour
        """
        self.vectorizer.fit_transform(self.corpus)
        names = self.vectorizer.get_feature_names()
        self.assertEqual(
            names, self.names
        )


if __name__ == "__main__":
    unittest.main()
