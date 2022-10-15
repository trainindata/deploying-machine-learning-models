# config
# feature encoding, missing values, imputation, etc.
from feature_engine.encoding import OneHotEncoder, RareLabelEncoder
from feature_engine.imputation import (
    AddMissingIndicator,
    CategoricalImputer,
    MeanMedianImputer,
)

# to build the models
from sklearn.linear_model import LogisticRegression

# Pipeline
from sklearn.pipeline import Pipeline

# feature scaling
from sklearn.preprocessing import StandardScaler

from classification_model.config.core import config

# customized feature transformation
from classification_model.processing import features as pp

# set up the pipeline
titanic_pipe = Pipeline(
    [
        # ===== IMPUTATION =====
        # impute categorical variables with string missing
        (
            "categorical_imputation",
            CategoricalImputer(
                imputation_method=config.model_config.str_imputation_method,
                variables=config.model_config.categorical_variables,
            ),
        ),
        # add missing indicator to numerical variables
        (
            "missing_indicator",
            AddMissingIndicator(variables=config.model_config.numerical_variables),
        ),
        # impute numerical variables with the median
        (
            "median_imputation",
            MeanMedianImputer(
                imputation_method=config.model_config.median_imputation_method,
                variables=config.model_config.numerical_variables,
            ),
        ),
        # Extract letter from cabin
        (
            "extract_letter",
            pp.ExtractLetterTransformer(
                variables=config.model_config.cabin_variable_parse
            ),
        ),
        # == CATEGORICAL ENCODING ======
        # remove categories present in less than 5% of the observations (0.05)
        # group them in one category called 'Rare'
        (
            "rare_label_encoder",
            RareLabelEncoder(
                tol=config.model_config.rare_label_encoder_tol,
                n_categories=config.model_config.rare_label_encoder_n_categories,
                variables=config.model_config.categorical_variables,
            ),
        ),
        # encode categorical variables using one hot encoding into k-1 variables
        (
            "categorical_encoder",
            OneHotEncoder(
                drop_last=True, variables=config.model_config.categorical_variables
            ),
        ),
        # scale
        ("scaler", StandardScaler()),
        (
            "Logit",
            LogisticRegression(
                C=config.model_config.C, random_state=config.model_config.random_state
            ),
        ),
    ]
)
