import numpy as np

from regression_model.predict import make_prediction


def test_make_prediction(sample_input_data):
    # When
    result = make_prediction(input_data=sample_input_data)

    # Then
    predictions = result.get("predictions")
    assert isinstance(predictions, list)
    assert isinstance(predictions[0], np.float64)
    assert result.get("errors") is None
