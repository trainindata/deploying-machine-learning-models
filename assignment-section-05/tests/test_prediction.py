import numpy as np

from classification_model.predict import make_prediction


def test_make_prediction(sample_input_data, first_ten_expected_predictions):
    # Given
    expected_no_predictions = 131

    # When
    result = make_prediction(input_data=sample_input_data)

    # Then
    predictions = result.get("predictions")
    assert isinstance(predictions, np.ndarray)
    assert isinstance(predictions[0], np.int64)
    assert result.get("errors") is None
    assert len(predictions) == expected_no_predictions
    assert list(predictions)[:10] == first_ten_expected_predictions
