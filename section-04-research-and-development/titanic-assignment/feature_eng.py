import numpy as np
import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin


class TemporalVariableTransformer(BaseEstimator, TransformerMixin):
    # Temporal elapsed time transformer

    def __init__(self, variables, references_variable) -> None:
        super().__init__()
        if not isinstance(variables, list):
            raise ValueError("Variables should be a list")
        self.variables = variables
        self.reference_variable = references_variable

    def fit(self, X, y=None):

        return self
    
    def transform(self, X):
        X = X.copy()

        for feature in self.variables:
            X[feature] = X[self.reference_variable] - X[feature]
        
        return X


class Mapper(BaseEstimator, TransformerMixin):

    def __init__(self, variables, mappings) -> None:
        
        if not isinstance(variables, list):
            raise ValueError("Variable should be a lsit")
        super().__init__()
        self.variables = variables
        self.mappings = mappings

    def fit(self, X, y=None):

        return self
    
    def transform(self, X):

        X = X.copy()
        for feature in self.variables:
            X[feature] = X[feature].map(self.mappings)
        
        return X


class MeanImputer(BaseEstimator, TransformerMixin):

    def __init__(self, variables) -> None:
        if not isinstance(variables, list):
            raise ValueError("Variables should be a list")
        self.variables = variables

    def fit(self, X, y=None):
        self.imputer_dict_ = X[self.variables].mean().to_dict()

        return self

    def transform(self, X):
        X = X.copy()
        for feature in self.variables:
            X[feature].fillna(self.imputer_dict_[feature], inplace=True)

        return X

    
    class RareLabelCategoricalEncoder(BaseEstimator, TransformerMixin):


        def __init__(self, tol=0.05, variables=None) -> None:

            if not isinstance(variables, list):
                raise ValueError("Variables should be a list")
            super().__init__()
            self.tol = tol
            self.variables = variables

        def fit(self, X, y=None):
            
            self.encoder_dict_ = {}
            for var in self.variables:
                t = pd.Series(X[var].value_counts(normalize=True))
                self.encoder_dict_[var] = list(t[t >= self.tol].index)
            
            return self
        
        def transform(self, X):
            X = X.copy()
            for feature in self.variables:
                X[feature] = np.where(X[feature].isin(self.encoder_dict_[feature]),
                 X[feature], "Rare")

            return X


class CategoricalEncoder(BaseEstimator, TransformerMixin):
    """String to numbers categorcal encoder"""

    def __init__(self, variables) -> None:
        if not isinstance(variables, list):
            raise ValueError("Variables should be a list")

        super().__init__()
        self.variables = variables

    def fit(self, X, y):
        temp = pd.concat([X, y], axis=1)
        temp.columns = list(X.columns) + ["target"]

        # persit transforming dictionary
        self.encoder_dict_ = {}

        for var in self.variables:
            t = temp.groupby([var])["target"].mean().sort_values(ascending=True).index
            self.encoder_dict_[var] = {k: i for i, k in enumerate(t,0)}

        return self


    def transform(self, X):
        # encode labels

        X = X.copy()
        for feature in self.variables:
            X[feature] = X[feature].map(self.encoder_dict_[feature])

        return X
    