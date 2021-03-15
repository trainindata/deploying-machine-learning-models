import pandas as pd

import joblib
import config


def make_prediction(input_data):
    
    _titanic_pipe = joblib.load(filename=config.PIPELINE_NAME)
    
    results = _titanic_pipe.predict(input_data)

    return results
   
if __name__ == '__main__':
    
    # test pipeline
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score

    data = pd.read_csv(config.TRAINING_DATA_FILE)

    X_train, X_test, y_train, y_test = train_test_split(
        data.drop(config.TARGET, axis=1),
        data[config.TARGET],
        test_size=0.2,
        random_state=0)  # we are setting the seed here
    
    pred = make_prediction(X_test)
    
    # determine the accuracy
    print('test accuracy: {}'.format(accuracy_score(y_test, pred)))
    print()

