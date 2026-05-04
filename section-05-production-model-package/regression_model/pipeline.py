from feature_engine.encoding import OrdinalEncoder, RareLabelEncoder
from feature_engine.imputation import AddMissingIndicator, CategoricalImputer, MeanMedianImputer
from feature_engine.selection import DropFeatures
from feature_engine.transformation import LogTransformer
from feature_engine.wrappers import SklearnTransformerWrapper
from sklearn.linear_model import Lasso
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Binarizer, MinMaxScaler

from regression_model.config.core import config
from regression_model.processing import features as pp

MAPPED_CATEGORICAL_VARS = (
    config.model_settings.qual_vars
    + config.model_settings.exposure_vars
    + config.model_settings.finish_vars
    + config.model_settings.garage_vars
)

ENCODING_CATEGORICAL_VARS = [
    var
    for var in config.model_settings.categorical_vars
    if var not in MAPPED_CATEGORICAL_VARS
]

price_pipe = Pipeline(
    [
        # ===== IMPUTATION =====
        # impute categorical variables with string missing
        (
            "missing_imputation",
            CategoricalImputer(
                imputation_method="missing",
                variables=config.model_settings.categorical_vars_with_na_missing,
            ),
        ),
        (
            "frequent_imputation",
            CategoricalImputer(
                imputation_method="frequent",
                variables=config.model_settings.categorical_vars_with_na_frequent,
            ),
        ),
        # add missing indicator
        (
            "missing_indicator",
            AddMissingIndicator(variables=config.model_settings.numerical_vars_with_na),
        ),
        # impute numerical variables with the mean
        (
            "mean_imputation",
            MeanMedianImputer(
                imputation_method="mean",
                variables=config.model_settings.numerical_vars_with_na,
            ),
        ),
        # == TEMPORAL VARIABLES ====
        (
            "elapsed_time",
            pp.TemporalVariableTransformer(
                variables=config.model_settings.temporal_vars,
                reference_variable=config.model_settings.ref_var,
            ),
        ),
        ("drop_features", DropFeatures(features_to_drop=[config.model_settings.ref_var])),
        # ==== VARIABLE TRANSFORMATION =====
        ("log", LogTransformer(variables=config.model_settings.numericals_log_vars)),
        (
            "binarizer",
            SklearnTransformerWrapper(
                transformer=Binarizer(threshold=0),
                variables=config.model_settings.binarize_vars,
            ),
        ),
        # === mappers ===
        (
            "mapper_qual",
            pp.Mapper(
                variables=config.model_settings.qual_vars,
                mappings=config.model_settings.qual_mappings,
            ),
        ),
        (
            "mapper_exposure",
            pp.Mapper(
                variables=config.model_settings.exposure_vars,
                mappings=config.model_settings.exposure_mappings,
            ),
        ),
        (
            "mapper_finish",
            pp.Mapper(
                variables=config.model_settings.finish_vars,
                mappings=config.model_settings.finish_mappings,
            ),
        ),
        (
            "mapper_garage",
            pp.Mapper(
                variables=config.model_settings.garage_vars,
                mappings=config.model_settings.garage_mappings,
            ),
        ),
        (
            "cast_encoding_categoricals",
            pp.CastVariablesAsObject(variables=ENCODING_CATEGORICAL_VARS),
        ),
        # == CATEGORICAL ENCODING
        (
            "rare_label_encoder",
            RareLabelEncoder(
                tol=0.01, n_categories=1, variables=ENCODING_CATEGORICAL_VARS
            ),
        ),
        # encode categorical variables using the target mean
        (
            "categorical_encoder",
            OrdinalEncoder(
                encoding_method="ordered",
                variables=ENCODING_CATEGORICAL_VARS,
            ),
        ),
        ("scaler", MinMaxScaler()),
        (
            "Lasso",
            Lasso(
                alpha=config.model_settings.alpha,
                random_state=config.model_settings.random_state,
            ),
        ),
    ]
)
