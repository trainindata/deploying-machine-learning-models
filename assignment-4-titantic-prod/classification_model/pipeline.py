from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

from feature_engine.imputation import (
    AddMissingIndicator,
    MeanMedianImputer,
    CategoricalImputer,
)

from feature_engine.encoding import (
    RareLabelEncoder,
    OneHotEncoder,
)

from classification_model.config.core import config
from classification_model.processing import features as pp


titanic_pipe = Pipeline([

    # ==== IMPUTATION ====
    # imputer categorical varaibles with string 'missing"
    ('categorical_imputation', CategoricalImputer(
        imputation_method="missing",
        variables=config.model_config.categorical_vars,
    )
    ),

    # add missing indicator to numerical variables
    ('missing_indicator', AddMissingIndicator(
        variables=config.model_config.numerical_vars
    )
    ),

    # imputer numerical variables with the median
    ('median_imputation', MeanMedianImputer(
        imputation_method="median",
        variables=config.model_config.numerical_vars
    )
    ),

    # ==== CATEGORICAL ENCODING ====
    # remove categories present in less than 5% of the obeservations
    # group thme into one category called 'Rare'
    ('rare_label_encoder', RareLabelEncoder(
        tol=config.model_config.tol,
        n_categories=config.model_config.n_categories,
        variables=config.model_config.categorical_vars,
    )
    ),

    # encode categorical variables using one-hot encoding into k-1 variables
    ('categorical_encoder', OneHotEncoder(
        variables=config.model_config.categorical_vars,
        drop_last=True,
    )
    ),

    # scale using standardization
    ('scaler', StandardScaler()),

    # logistic regression
    ('Logit', LogisticRegression(
        C=config.model_config.c,
        random_state=config.model_config.random_state,
    )
    ),
])