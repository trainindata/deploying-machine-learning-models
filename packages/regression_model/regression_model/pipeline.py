from sklearn.pipeline import Pipeline
from sklearn.linear_model import Lasso
from sklearn.preprocessing import MinMaxScaler
#import sys
#sys.path.append('..')
from regression_model.processing import preprocessors as pp
from regression_model.config import config
from regression_model.processing import features

price_pipe = Pipeline(
    [
        ('categorical_imputer',
         pp.CategoricalImputer(variables=config.CATEGORICAL_VARS)),
        ('numerical_imputer', 
        pp.NumericalImputer(variables=config.NMERICAL_VARS_WITH_NA)),
        ('temporal_variable',
        pp.TemporalVariableEstimator(variables=config.TEMPORAL_VARS,
        reference_variable=config.DROP_FEATURES)),
        ('rare_label_encoder',
        pp.RareLabelCategoricalEncoder(tol=0.01,variables=config.CATEGORICAL_VARS)),
        ('categorical_encoder',
        pp.CategoricalEncoder(variables=config.CATEGORICAL_VARS)),
        ('log_transformer',
        features.LogTransformer(variables=config.NUMERICAL_LOG_VARS)),
        ('drop_features',
        pp.DropUnecessaryFeatures(variables_to_drop=config.DROP_FEATURES)),
        ('scaler',
        MinMaxScaler()),
        ('linear_model', Lasso(alpha=0.005, random_state=0))
    ])

