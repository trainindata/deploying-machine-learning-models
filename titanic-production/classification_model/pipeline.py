from feature_engine.encoding import OneHotEncoder, RareLabelEncoder
from feature_engine.imputation import AddMissingIndicator, CategoricalImputer, MeanMedianImputer
from feature_engine.selection import DropFeatures
from feature_engine.transformation import LogTransformer
from feature_engine.wrappers import SklearnTransformerWrapper
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from classification_model.config.core import config
from classification_model.processing import features as pp
from classification_model.processing.features import ExtractLetterTransformer

titanic_pipe = Pipeline(
    [
        # ===== IMPUTATION =====
        # impute categorical variables with string missing
        (
            "categorical_imputation",
            CategoricalImputer(
                imputation_method="missing",
                variables=config.model_config.categorical_variables,
            )
        ),

        # Add missing indicator to numerical variables
        (
            "missing_indicator",
            AddMissingIndicator(
                variables=config.model_config.numerical_variables
            )
        ),

        # Impute numerical variables with the median
        (
            "median_imputation",
            MeanMedianImputer(
                imputation_method="median",
                variables=config.model_config.numerical_variables
            )
        ),

        # Extract letter from cabin
        (
            "extract_letter",
            ExtractLetterTransformer(
                variables=config.model_config.cabin_var
            )
        ),

        # === CATEGORICAL ENCODING ===
        # Remove categories present in less than 5% of the observations
        # group them in one category called 'Rare'
        (
            "rare_label_encoder",
            RareLabelEncoder(
                tol=0.05,
                n_categories=1,
                variables=config.model_config.categorical_variables
            )
        ),

        # Encode categorical variables using one hot encoding into k-1 variables
        (
            "categorical_encoder",
            OneHotEncoder(
                drop_last=True,
    	        variables=config.model_config.categorical_variables
            )
        ),

        # Scale
        (
            "scaler",
            StandardScaler(),
        ),

        # Classification model
        (
            "Logit",
            LogisticRegression(
                C=config.model_config.C,
                random_state=config.model_config.random_state
                )
        )
        
    ]
)
