import math
import os

import numpy as np

from regression_model.predict import make_prediction

ACCEPTABLE_MODEL_DIFFERENCE = float(os.environ.get("ACCEPTABLE_MODEL_DIFFERENCE"))


def test_compare_against_research_environment_predictions(
    research_model_results, sample_input_data
):
    # Given
    expected_no_predictions = len(research_model_results)

    # When
    result = make_prediction(input_data=sample_input_data)

    # Then
    package_predictions = result.get("predictions")
    assert isinstance(package_predictions, list)
    assert isinstance(package_predictions[0], np.float64)
    assert result.get("errors") is None
    assert len(package_predictions) == expected_no_predictions

    # Compare research vs. package predictions
    for package_prediction, research_prediction in zip(
        package_predictions, research_model_results.values
    ):

        # convert str to float.
        previous_value = float(package_prediction)
        current_value = float(research_prediction)

        # rel_tol is the relative tolerance – it is the maximum allowed
        # difference between a and b, relative to the larger absolute
        # value of a or b. For example, to set a tolerance of 5%, pass
        # rel_tol=0.05.
        assert math.isclose(
            previous_value, current_value, rel_tol=ACCEPTABLE_MODEL_DIFFERENCE
        )
