import math

import pandas as pd

from classification_model.predict import make_prediction


def test_make_prediction(sample_input_data):
    # Given
    # TODO: fill in value
    # expected_first_prediction_value =
    # expected_num_predictions =

    # When
    result = make_prediction(input_data=sample_input_data)

    # checks
    predictions = result.get("predictions")
    assert isinstance(predictions, list)
    assert isinstance(predictions[0], float)
    assert result.get("errors") is None
    assert len(predictions) == expected_num_predictions # Need to fill expectation above
    assert predictions[0] == expected_first_prediction_value # Need to fill expectation above
