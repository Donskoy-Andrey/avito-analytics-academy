"""
Base classes for vectorizers
"""

from typing import List
from dataclasses import dataclass
from abc import ABC, abstractmethod
import numpy as np


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


@dataclass
class BaseTestClass:
    """
    Class with standard texts to text vectorizers
    """
    corpus = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste"
    ]
    count_matrix = [
        [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    ]
    names = [
        "crock", "pot", "pasta", "never", "boil", "again",
        "pomodoro", "fresh", "ingredients", "parmesan", "to", "taste"
    ]
    term_frequency = np.array(
        [
            [0.14285714285714285, 0.14285714285714285, 0.2857142857142857,
             0.14285714285714285, 0.14285714285714285, 0.14285714285714285,
             0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.14285714285714285, 0.0, 0.0, 0.0, 0.14285714285714285,
             0.14285714285714285, 0.14285714285714285, 0.14285714285714285,
             0.14285714285714285, 0.14285714285714285]
        ]
    )
    inverse_df = np.array([
        1.4054651081081644, 1.4054651081081644, 1.0, 1.4054651081081644,
        1.4054651081081644, 1.4054651081081644, 1.4054651081081644,
        1.4054651081081644, 1.4054651081081644, 1.4054651081081644,
        1.4054651081081644, 1.4054651081081644
    ])
    tf_idf = np.array([
        [[0.20078072972973776, 0.20078072972973776, 0.2857142857142857,
          0.20078072972973776, 0.20078072972973776,
          0.20078072972973776, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
         [0.0, 0.0, 0.14285714285714285, 0.0, 0.0, 0.0, 0.20078072972973776,
          0.20078072972973776, 0.20078072972973776, 0.20078072972973776,
          0.20078072972973776, 0.20078072972973776]]
    ])
