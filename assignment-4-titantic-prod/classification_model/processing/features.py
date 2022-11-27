import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class ExtractLetterTransformer(BaseEstimator, TransformerMixin):
    """
    Extracts the first letter of a variable.
    """

    def __init__(self, varialbes):
        if not isinstance(variables, list):
            raise ValueError(
                f"variables should be a list. Got {variables} instead."
            )

        self.variables = variables

    def fit(sel, X, y=None):
        # need to meet sklearn pipeline requirements

    def transform(self, X):
        X = X.copy()

        for var in self.variables:
            X[var] = X[feature].str[0]

        return X