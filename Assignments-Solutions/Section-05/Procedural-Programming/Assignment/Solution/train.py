import preprocessing_functions as pf
import config

# ================================================
# TRAINING STEP - IMPORTANT TO PERPETUATE THE MODEL

# Load data
data = pf.load_data(config.PATH_TO_DATASET)

# divide data set
X_train, X_test, y_train, y_test = pf.divide_train_test(data, config.TARGET)

# get first letter from cabin variable
X_train['cabin'] = pf.extract_cabin_letter(X_train, 'cabin')

# impute categorical variables
for var in config.CATEGORICAL_VARS:
    X_train[var] = pf.impute_na(X_train, var, replacement='Missing')

# impute numerical variable
for var in config.NUMERICAL_TO_IMPUTE:
    
    # add missing indicator first
    X_train[var + '_NA'] = pf.add_missing_indicator(X_train, var)
    
    # impute NA
    X_train[var] = pf.impute_na(X_train, var, 
           replacement = config.IMPUTATION_DICT[var])


# Group rare labels
for var in config.CATEGORICAL_VARS:
    X_train[var] = pf.remove_rare_labels(X_train, var,
           config.FREQUENT_LABELS[var])


# encode categorical variables
for var in config.CATEGORICAL_VARS:
    X_train = pf.encode_categorical(X_train, var)


# check all dummies were added
X_train = pf.check_dummy_variables(X_train, config.DUMMY_VARIABLES)


# train scaler and save
scaler = pf.train_scaler(X_train,
                         config.OUTPUT_SCALER_PATH)

# scale train set
X_train = scaler.transform(X_train)

# train model and save
pf.train_model(X_train,
               y_train,
               config.OUTPUT_MODEL_PATH)


print('Finished training')