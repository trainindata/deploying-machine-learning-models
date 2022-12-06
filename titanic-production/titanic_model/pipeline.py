from feature_engine.encoding import OneHotEncoder, RareLabelEncoder
from feature_engine.imputation import (
    AddMissingIndicator,
    CategoricalImputer,
    MeanMedianImputer,
)
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from titanic_model.config.core import config
from titanic_model.processing import features as pp

survivor_pipe = Pipeline(
    [
        # ===== IMPUTATION =====
        # impute categorical variables with string missing
        (
            "categorical_imputation",
            CategoricalImputer(
                imputation_method="missing",
                variables=config.model_config.categorical_vars,
            ),
        ),
        # add missing indicator
        (
            "missing_indicator",
            AddMissingIndicator(variables=config.model_config.numerical_vars),
        ),
        # impute numerical variables with the median
        (
            "median_imputation",
            MeanMedianImputer(
                imputation_method="median",
                variables=config.model_config.numerical_vars,
            ),
        ),
        # ==== MODIFY VARIABLES ====
        # extract first letter from cabin
        (
            "extract_letter",
            pp.ExtractLetterTransformer(
                variables=config.model_config.extract_letter_vars
            ),
        ),
        # === CATEGORICAL ENCODING ===
        # remove categories present in less than 5% of the observations (0.05)
        # group them in one category called 'Rare'
        (
            "rare_label_encoder",
            RareLabelEncoder(
                tol=0.05, n_categories=1, variables=config.model_config.categorical_vars
            ),
        ),
        # encode categorical variables using the target mean
        (
            "categorical_encoder",
            OneHotEncoder(
                drop_last=True,
                variables=config.model_config.categorical_vars,
            ),
        ),
        # == SCALING ==
        ("scaler", StandardScaler()),
        # = LOGISTIC REGRESSION =
        (
            "LogReg",
            LogisticRegression(
                C=config.model_config.logistic_regression_C,
                random_state=config.model_config.seed,
            ),
        ),
    ]
)
