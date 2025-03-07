import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from classification_model.config.core import config
from classification_model.predict import make_prediction


def test_make_prediction(sample_input_data):
    expected_no_predictions = 131

    X_train, X_test, y_train, y_test = train_test_split(
        sample_input_data[config.model_config.features],  # predictors
        sample_input_data[config.model_config.target],
        test_size=config.model_config.test_size,
        # we are setting the random seed here
        # for reproducibility
        random_state=config.model_config.random_state,
    )

    result = make_prediction(input_data=X_test)
    predictions = result.get("predictions")
    assert isinstance(predictions, np.ndarray)
    assert isinstance(predictions[0], np.int64)
    assert result.get("errors") is None
    assert len(predictions) == expected_no_predictions
    _predictions = list(predictions)
    accuracy = accuracy_score(y_test, _predictions)
    assert accuracy > 0.7
