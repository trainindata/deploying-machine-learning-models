
from sklearn.base import BaseEstimator, TransformerMixin


class ExtractLetterTransformer(BaseEstimator, TransformerMixin):
    # Extract the first letter of a variable

    def __init__ (self, variables):
        if not isinstance(variables, list):
            raise ValueError("Variables should be a list.")

        self.variables = variables

    def fit(self, X, y=None):
        # This step is needed. Sklearn standard pipeline (they need a fit() method)
        return self
    
    def transform(self, X):
        # Do not overwrite original dataframe
        X = X.copy()

        for feature in self.variables:
            X[feature] = X[feature].str[0]

        return X
