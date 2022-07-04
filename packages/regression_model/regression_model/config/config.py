import pathlib




PACKAGE_ROOT = pathlib.Path(__file__).resolve().parent.parent
TRAINED_MODEL_DIR = PACKAGE_ROOT / 'trained_models'
DATASET_DIR = PACKAGE_ROOT / 'datasets'
LOG_DIR = PACKAGE_ROOT/'logs'
TESTING_DATA_FILE = 'test.csv'
TRAINING_DATA_FILE = 'train.csv'
TARGET = 'SalePrice'


FEATURES = ['MSSubClass', 'MSZoning', 'Neighborhood', 'OverallQual',
            'OverallCond', 'YearRemodAdd', 'RoofStyle', 'MasVnrType',
            'BsmtQual', 'BsmtExposure', 'HeatingQC', 'CentralAir',
            '1stFlrSF', 'GrLivArea', 'BsmtFullBath', 'KitchenQual',
            'Fireplaces', 'FireplaceQu', 'GarageType', 'GarageFinish',
            'GarageCars', 'PavedDrive', 'LotFrontage',
            # this variable is only to calculate temporal variable:
            'YrSold']


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

CATEGORICAL_VARS_WITH_NA = [
    "MasVnrType",
    "BsmtQual",
    "BsmtExposure",
    "FireplaceQu",
    "GarageType",
    "GarageFinish",
]

NUMERICAL_NA_NOT_ALLOWED = [
    feature
    for feature in FEATURES
    if feature not in CATEGORICAL_VARS + NMERICAL_VARS_WITH_NA
]

CATEGORICAL_NA_NOT_ALLOWED = [
    feature for feature in CATEGORICAL_VARS if feature not in CATEGORICAL_VARS_WITH_NA
]

PIPELINE_NAME = 'lasso_regression'

PIPELINE_SAVE_FILE = 'regression_model'
