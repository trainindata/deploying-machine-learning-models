# ====   PATHS ===================

TRAINING_DATA_FILE = "titanic.csv"
PIPELINE_NAME = 'logistic_regression.pkl'


# ======= FEATURE GROUPS =============

TARGET = 'survived'

CATEGORICAL_VARS = ['sex', 'cabin', 'embarked', 'title']

NUMERICAL_VARS = ['age', 'fare']

CABIN = 'cabin'