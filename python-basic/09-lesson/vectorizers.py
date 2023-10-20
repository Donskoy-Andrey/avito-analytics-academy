"""
Module with CountVectorizer class
"""
import math
from typing import List
from base import BaseModel, CountVectorizerError


class CountVectorizer(BaseModel):
    """
    Analogue for sklearn.feature_extraction.text.CountVectorizer
    Source: https://clck.ru/UVrqa
    """

    def __init__(self):
        self.feature_names = None

    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        """
        Learn the vocabulary dictionary and return document-term matrix.

        :return:
            Document-term matrix in list[list[int]] format.
        """

        # Count amount of words
        alphabet = {}
        for text in corpus:
            text = text.lower()
            for word in text.strip().split():
                if alphabet.get(word) is None:
                    alphabet[word] = len(alphabet)

        count_matrix = []
        for text in corpus:
            text = text.lower()
            bag = [0] * len(alphabet)
            for word in text.strip().split():
                index = alphabet[word]
                bag[index] += 1
            count_matrix.append(bag)

        self.feature_names = list(alphabet.keys())
        return count_matrix

    def get_feature_names(self) -> List[str]:
        """
        Get output feature names for transformation.

        :raise CountVectorizerError: if called before `fit_transform`.
        :return:
            Feature names in list[str] format.
        """
        if self.feature_names is None:
            exception_text = (
                "`Get_feature_names` method should be called"
                " after `fit_transform` method."
            )
            raise CountVectorizerError(exception_text)
        return self.feature_names


class TfIdfTransformer:
    """
    Class that combine static methods
    to make TF-IDF preprocessing
    """

    @staticmethod
    def tf_transform(
        count_matrix: list[list[int]]
    ) -> list[list[float]]:
        """
        Create term frequency list

        :return:
            term frequency for all texts
        """

        term_frequency = []
        for text in count_matrix:
            words = sum(text)

            term_frequency.append(
                [word_amount / words for word_amount in text]
            )

        return term_frequency

    @staticmethod
    def idf_transform(
        count_matrix: list[list[int]]
    ) -> list[float]:
        """
        Create inverse document frequency list

        :return:
            Inverse document frequency for all texts.
        """

        idf = []
        all_docs = len(count_matrix)

        for entry in zip(*count_matrix):
            docs_with_word = len([doc for doc in entry if doc > 0])

            idf.append(
                math.log((all_docs + 1) / (docs_with_word + 1)) + 1
            )

        return idf

    @staticmethod
    def tf_idf(
        term_frequency: list[list[float]], idf: list[float]
    ) -> list[list[float]]:
        """
        Create tf-idf matrix

        :param term_frequency: result of `tf_transform` function
        :param idf: result of `idf_transform` function
        :return:
            tf-idf matrix
        """
        tf_idf_matrix = []

        for term in term_frequency:
            tf_idf_matrix.append(
                list(
                    map(
                        lambda pair: pair[0] * pair[1],
                        list(zip(term, idf))
                    )
                )
            )

        return tf_idf_matrix


class TfIdfVectorizer(CountVectorizer):
    """
    Class that can implement TF-IDF to the corpus of text
    """

    def __init__(self):
        super().__init__()
        self.transformer = TfIdfTransformer()

    def fit_transform(self, corpus: List[str]) -> list[list[float]]:
        """
        Create tf-idf matrix

        :param corpus: list of texts
        :return:
            tf-idf matrix for these texts
        """

        count_matrix = super().fit_transform(corpus)
        term_frequency = self.transformer.tf_transform(count_matrix)
        inverse_df = self.transformer.idf_transform(count_matrix)
        tf_idf = self.transformer.tf_idf(term_frequency, inverse_df)
        return tf_idf
