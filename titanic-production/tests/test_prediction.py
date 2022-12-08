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
    # get predictions from dict
    predictions = result.get("predictions")

    # check that there are no errors
    assert result.get("errors") is None

    # check the predictions are a numpy ndarray
    assert isinstance(predictions, np.ndarray)
    # check that the first value predicted is an integer
    assert isinstance(predictions[0], np.int64)
    # check that the expected number of predictions is as specified before
    assert len(predictions) == expected_no_predictions

    y_true = sample_input_data[config.model_config.target]

    # test predictions
    assert predictions[6] == 0
    assert predictions[34] == 1
    assert predictions[72] == 0
    assert predictions[120] == 0
    assert predictions[194] == 0

    # test accuracy
    accuracy = accuracy_score(list(predictions), y_true)
    print(f"\n-------------\nACCURACY: {accuracy}")
    assert accuracy > config.model_config.expected_accuracy
