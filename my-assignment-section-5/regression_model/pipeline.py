from feature_engine.encoding import RareLabelEncoder, OneHotEncoder
from feature_engine.imputation import (
    AddMissingIndicator,
    CategoricalImputer,
    MeanMedianImputer,
)
from regression_model.processing.features import ExtractLetterTransformer

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression

from regression_model.config.core import config

price_pipe = Pipeline(
    [

    # ===== IMPUTATION =====
    # impute categorical variables with string missing
    ('categorical_imputation', CategoricalImputer(
        imputation_method='missing', variables=config.model_config.categorical_variables)),

    # add missing indicator to numerical variables
    ('missing_indicator', AddMissingIndicator(variables=config.model_config.numerical_variables)),

    # impute numerical variables with the median
    ('median_imputation', MeanMedianImputer(
        imputation_method='median', variables=config.model_config.numerical_variables)),


    # Extract letter from cabin
    ('extract_letter', ExtractLetterTransformer(variables=[config.model_config.cabin_variable])),


    # == CATEGORICAL ENCODING ======
    # remove categories present in less than 5% of the observations (0.05)
    # group them in one category called 'Rare'
    ('rare_label_encoder', RareLabelEncoder(
        tol=config.model_config.rare_label_encoder_threshold,
        n_categories=config.model_config.rare_label_encoder_n_categories,
        variables=config.model_config.categorical_variables)),


    # encode categorical variables using one hot encoding into k-1 variables
    ('categorical_encoder', OneHotEncoder(
        drop_last=config.model_config.drop_last, variables=config.model_config.categorical_variables)),

    # scale
    ('scaler', StandardScaler()),

    ('Logit', LogisticRegression(C=config.model_config.logistic_regression_c, random_state=config.model_config.random_state)),
    ]
)
