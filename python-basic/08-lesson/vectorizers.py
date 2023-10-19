"""
Module with CountVectorizer class
"""
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


if __name__ == "__main__":
    model = CountVectorizer()
    print(model.fit_transform.__doc__)
