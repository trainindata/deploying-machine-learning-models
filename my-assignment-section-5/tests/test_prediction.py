import math

import numpy as np

from regression_model.predict import make_prediction
from regression_model.config.core import config


def test_make_prediction(sample_input_data):
    # Given
    expected_first_prediction_value = 2.7
    expected_no_predictions = 1309

    # When
    result = make_prediction(input_data=sample_input_data)


    # Then
    predictions = result.get("predictions")
    assert isinstance(predictions, list)
    assert isinstance(predictions[0], np.float64)
    assert result.get("errors") is None
    assert len(predictions) == expected_no_predictions
    assert math.isclose(predictions[0], expected_first_prediction_value, abs_tol=0.1)

def test_accuracy(sample_input_data):

    result = make_prediction(input_data=sample_input_data)

    predictions = result.get("predictions")

    target = np.exp(sample_input_data[config.model_config.target].values)

    accuracy = np.sum(target==predictions) / len(target)

    print(accuracy)

    assert accuracy > 0.7
