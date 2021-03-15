import preprocessing_functions as pf
import config

# =========== scoring pipeline =========

# impute categorical variables
def predict(data):
    
    # extract first letter from cabin
    data['cabin'] = pf.extract_cabin_letter(data, 'cabin')

    # impute NA categorical
    for var in config.CATEGORICAL_VARS:
        data[var] = pf.impute_na(data, var, replacement='Missing')
    
    
    # impute NA numerical
    for var in config.NUMERICAL_TO_IMPUTE:
        
        # add missing indicator first
        data[var + '_NA'] = pf.add_missing_indicator(data, var)
        
        # impute NA
        data[var] = pf.impute_na(data, var, 
               replacement = config.IMPUTATION_DICT[var])
    
    
    # Group rare labels
    for var in config.CATEGORICAL_VARS:
        data[var] = pf.remove_rare_labels(data, var, config.FREQUENT_LABELS[var])
    
    # encode variables
    for var in config.CATEGORICAL_VARS:
        data = pf.encode_categorical(data, var)
        
        
    # check all dummies were added
    data = pf.check_dummy_variables(data, config.DUMMY_VARIABLES)

    
    # scale variables
    data = pf.scale_features(data,
                             config.OUTPUT_SCALER_PATH)
    
    # make predictions
    predictions = pf.predict(data, config.OUTPUT_MODEL_PATH)
    
    return predictions

# ======================================
    
# small test that scripts are working ok
    
if __name__ == '__main__':
        
    from sklearn.metrics import accuracy_score    
    import warnings
    warnings.simplefilter(action='ignore')
    
    # Load data
    data = pf.load_data(config.PATH_TO_DATASET)
    X_train, X_test, y_train, y_test = pf.divide_train_test(data,
                                                            config.TARGET)
    
    pred = predict(X_test)
    
    # evaluate
    print('test accuracy: {}'.format(accuracy_score(y_test, pred)))
    print()
        