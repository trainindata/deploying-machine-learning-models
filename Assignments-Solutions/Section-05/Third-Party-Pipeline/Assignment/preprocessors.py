import numpy as np
import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin


# Add binary variable to indicate missing values
class MissingIndicator(BaseEstimator, TransformerMixin):

    def __init__(self, variables=None):
        pass


    def fit(self, X, y=None):
        # to accommodate sklearn pipeline functionality
        pass


    def transform(self, X):
        # add indicator
        X = X.copy()
        pass


# categorical missing value imputer
class CategoricalImputer(BaseEstimator, TransformerMixin):

    def __init__(self, variables=None):
        pass

    def fit(self, X, y=None):
        # we need the fit statement to accommodate the sklearn pipeline
        pass

    def transform(self, X):
        X = X.copy()
        pass


# Numerical missing value imputer
class NumericalImputer(BaseEstimator, TransformerMixin):

    def __init__(self, variables=None):
        pass

    def fit(self, X, y=None):
        # persist mode in a dictionary
        self.imputer_dict_ = {}
        pass

    def transform(self, X):

        X = X.copy()
        pass


# Extract first letter from string variable
class ExtractFirstLetter(BaseEstimator, TransformerMixin):

    def __init__(self, variables=None):
        pass

    def fit(self, X, y=None):
        # we need this step to fit the sklearn pipeline
        pass

    def transform(self, X):
        X = X.copy()
        pass

# frequent label categorical encoder
class RareLabelCategoricalEncoder(BaseEstimator, TransformerMixin):

    def __init__(self, tol=0.05, variables=None):
        pass

    def fit(self, X, y=None):

        # persist frequent labels in dictionary
        self.encoder_dict_ = {}
        pass

    def transform(self, X):
        X = X.copy()
        pass


# string to numbers categorical encoder
class CategoricalEncoder(BaseEstimator, TransformerMixin):

    def __init__(self, variables=None):
        pass

    def fit(self, X, y=None):

        # HINT: persist the dummy variables found in train set
        self.dummies = pd.get_dummies(X[self.variables], drop_first=True).columns
        
        return self

    def transform(self, X):
        # encode labels
        X = X.copy()
        # get dummies
        
        # drop original variables

        # add missing dummies if any


        return X
