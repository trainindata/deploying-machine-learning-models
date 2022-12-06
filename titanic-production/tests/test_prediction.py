import numpy as np
from sklearn.metrics import accuracy_score

from titanic_model.config.core import config
from titanic_model.predict import make_prediction


def test_make_prediction(sample_input_data):
    # Given
    expected_no_total_dataset = 1309  # entire dataset
    expected_no_predictions = round(
        config.model_config.test_size
        * expected_no_total_dataset  # test size * total dataset
    )

    # When
    result = make_prediction(input_data=sample_input_data)

    # Then
    predictions = result.get("predictions")
    assert isinstance(predictions, np.ndarray)
    assert isinstance(predictions[0], np.int64)
    assert result.get("errors") is None
    assert len(predictions) == expected_no_predictions
    y_true = sample_input_data[config.model_config.target]
    accuracy = accuracy_score(list(predictions), y_true)
    print(f"\n-------------\nACCURACY: {accuracy}")
    assert accuracy > config.model_config.expected_accuracy
