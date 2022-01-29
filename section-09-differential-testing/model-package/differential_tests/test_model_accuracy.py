import os

import numpy as np
from regression_model.predict import make_prediction


def test_make_prediction(sample_input_data, persist_results):
    # Given
    expected_first_prediction_value = 113422
    expected_no_predictions = 1449

    # When
    result = make_prediction(input_data=sample_input_data)

    # Then
    predictions = result.get("predictions")
    assert isinstance(predictions, list)
    assert isinstance(predictions[0], np.float64)
    assert result.get("errors") is None
    assert len(predictions) == expected_no_predictions

    # Persist for comparison
    _predictions = list(predictions)
    label = os.environ.get("DIFF_TEST")
    with open(f"{label}_predictions.txt", "w") as handler:
        for prediction in _predictions:
            handler.write(f"{prediction}\n")
