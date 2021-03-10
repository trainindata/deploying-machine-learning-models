from sklearn.linear_model import Lasso
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder

from regression_model.processing import preprocessing as pp
from regression_model.config.core import config


price_pipe = Pipeline(
    [
        (
            "numerical_imputer",
            pp.SklearnTransformerWrapper(
                variables=config.model_config.numerical_vars,
                transformer=SimpleImputer(strategy="most_frequent"),
            ),
        ),
        (
            "categorical_encoder",
            pp.SklearnTransformerWrapper(
                variables=config.model_config.categorical_vars,
                transformer=OrdinalEncoder(),
            ),
        ),
        (
            "drop_features",
            pp.DropUnecessaryFeatures(
                variables_to_drop=config.model_config.drop_features,
            ),
        ),
        (
            ("Linear_model",
             Lasso(alpha=config.model_config.random_state, random_state=config.model_config.random_state))
        ),
    ]
)