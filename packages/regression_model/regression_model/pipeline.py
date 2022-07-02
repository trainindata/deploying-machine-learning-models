from sklearn.pipeline import Pipeline
from sklearn.linear_model import Lasso
from sklearn.preprocessing import MinMaxScaler

import preprocessors as pp


CATEGORICAL_VARS = ['MSZoning',
                    'Neighborhood',
                    'RoofStyle',
                    'MasVnrType',
                    'BsmtQual',
                    'BsmtExposure',
                    'HeatingQC',
                    'CentralAir',
                    'KitchenQual',
                    'FireplaceQu',
                    'GarageType',
                    'GarageFinish',
                    'PavedDrive']

TEMPORAL_VARS =  'YearRemodAdd'

DROP_FEATURES = 'YrSold'

NUMERICAL_LOG_VARS = ['LotFrontage', '1stFlrSF', 'GrLivArea']

NMERICAL_VARS_WITH_NA = ['LotFrontage']

CATEGORICAL_VARS = ['MSZoning',
                    'Neighborhood',
                    'RoofStyle',
                    'MasVnrType',
                    'BsmtQual',
                    'BsmtExposure',
                    'HeatingQC',
                    'CentralAir',
                    'KitchenQual',
                    'FireplaceQu',
                    'GarageType',
                    'GarageFinish',
                    'PavedDrive']
PIPELINE_NAME = 'lasso_regression'

price_pipe = Pipeline(
    [
        ('categorical_imputer',
         pp.CategoricalImputer(variables=CATEGORICAL_VARS)),
        ('numerical_imputer', 
        pp.NumericalImputer(variables=NMERICAL_VARS_WITH_NA)),
        ('temporal_variable',
        pp.TemporalVariableEstimator(variables=TEMPORAL_VARS,
        reference_variable=DROP_FEATURES)),
        ('rare_label_encoder',
        pp.RareLabelCategoricalEncoder(tol=0.01,variables=CATEGORICAL_VARS)),
        ('categorical_encoder',
        pp.CategoricalEncoder(variables=CATEGORICAL_VARS)),
        ('log_transformer',
        pp.LogTransformer(variables=NUMERICAL_LOG_VARS)),
        ('drop_features',
        pp.DropUnecessaryFeatures(variables_to_drop=DROP_FEATURES)),
        ('scaler',
        MinMaxScaler()),
        ('linear_model', Lasso(alpha=0.005, random_state=0))
    ])

