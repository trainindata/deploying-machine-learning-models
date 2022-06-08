
import numpy as np

from regression_model.predict import make_prediction
from sklearn.metrics import accuracy_score, roc_auc_score


def test_make_prediction(test_features):

    # When
    result = make_prediction(input_data=test_features)

    # Then
    predictions = result.get("predictions")
    assert isinstance(predictions, np.ndarray)
    #print(predictions.dtype)
    assert isinstance(predictions[0], np.int64)
    assert len(predictions) == len(test_features)

    counts = np.unique(predictions, return_counts=True)

    assert (counts[0] == [0, 1]).all()
    assert (counts[1] == [237, 25]).all()

    assert result.get("errors") is None


def test_accuracy(test_features, test_outcome):

    result = make_prediction(input_data=test_features)

    assert result.get("errors") is None

    accuracy = accuracy_score(test_outcome, result.get("predictions"))

    assert accuracy > 0.71 and accuracy < 0.72
