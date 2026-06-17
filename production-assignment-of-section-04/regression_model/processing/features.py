from sklearn.base import BaseEstimator, TransformerMixin

import pandas as pd
from typing import List

class ExtractLetterTransformer(BaseEstimator, TransformerMixin):
    """ Extract fist letter of variable. """

    def __init__(self, variables: List[str]):
        self.variables = variables

    def fit(self, X, y: pd.Series = None):
        return self
        
    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X = X.copy()
        for var in self.variables:
            X[var] = X[var].str[0]

        return X