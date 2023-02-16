import math

from classification_model.predict import make_prediction


def test_make_prediction(sample_input_data):
    # Given
    expected_first_prediction_value = 0
    expected_no_predictions = 418
    # When
    result = make_prediction(input_data=sample_input_data)
    # Then
    predictions = result.get("predictions")
    predict_proba = result.get("predict_proba")
    # print(f"Predictions {predictions}")
    assert isinstance(predictions, list)
    assert isinstance(predict_proba[0], float)
    assert result.get("errors") is None
    assert len(predictions) == expected_no_predictions
    assert math.isclose(predictions[0], expected_first_prediction_value)
