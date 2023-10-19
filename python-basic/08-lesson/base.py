"""
Base classes for vectorizers
"""


from abc import ABC, abstractmethod
from typing import List


class CountVectorizerError(Exception):
    """
    Exception in CountVectorizer class.
    """


class BaseModel(ABC):
    """
    Abstract class for models
    """

    @abstractmethod
    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        """
        Abstract method for vectorizer fit-transform.

        :return:
            Document-term matrix in list[list[int]] format.
        """

    @abstractmethod
    def get_feature_names(self) -> List[str]:
        """
        Abstract method to get feature names after vectorizer transform.

        :return:
            Feature names in list[str] format.
        """
