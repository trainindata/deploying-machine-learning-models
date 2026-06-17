# import libraries
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from feature_engine.imputation import CategoricalImputer, MeanMedianImputer, AddMissingIndicator
from feature_engine.creation import ExtractLetterTransformer
from sklearn.pipeline import Pipeline
from feature_engine.encoding import RareLabelEncoder, OneHotEncoder as FeOneHotEncoder

from regression_model.config.core import config

# set up the pipeline
titanic_pipe = Pipeline([

    # ===== IMPUTATION =====
    # impute categorical variables with string 'missing'
    ('categorical_imputation', CategoricalImputer(fill_value='Missing', variables=config.model_config.categorical_vars)),

    # add missing indicator to numerical variables
    ('missing_indicator', AddMissingIndicator(variables=config.model_config.numerical_vars)),

    # impute numerical variables with the median
    ('median_imputation', MeanMedianImputer(imputation_method='median', variables=config.model_config.numerical_vars)),

    # Extract first letter from cabin
    ('extract_letter', ExtractLetterTransformer(variables=config.model_config.letter_extraction_vars)),

    # == CATEGORICAL ENCODING ======
    # remove categories present in less than 5% of the observations (0.05)
    # group them in one category called 'Rare'
    ('rare_label_encoder', RareLabelEncoder(tol=0.05, variables=config.model_config.categorical_vars)),

    # encode categorical variables using one hot encoding into k-1 variables
    ('categorical_encoder', FeOneHotEncoder(drop_last=True, variables=config.model_config.categorical_vars)),

    # scale using standardization
    ('scaler', StandardScaler()),

    # logistic regression (use C=0.0005 and random_state=0)
    ('Logit', LogisticRegression(C=0.0005, random_state=0)),
])