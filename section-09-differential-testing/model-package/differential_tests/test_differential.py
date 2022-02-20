import math
import os
from pathlib import Path

ACCEPTABLE_MODEL_DIFFERENCE = float(os.environ.get("ACCEPTABLE_MODEL_DIFFERENCE"))


def test_difference_between_current_and_candidate_models(sample_input_data):
    # Given
    persisted_results_dir = Path(__file__).resolve().parent.parent
    with open(persisted_results_dir / "current_predictions.txt", "r") as handler:
        current_predictions = [line.rstrip() for line in handler]

    with open(persisted_results_dir / "candidate_predictions.txt", "r") as handler:
        candidate_predictions = [line.rstrip() for line in handler]

    # When
    assert len(candidate_predictions) == len(current_predictions)

    # Perform the differential test
    for previous_value, current_value in zip(
        current_predictions, candidate_predictions
    ):

        # convert str to float.
        previous_value = float(previous_value)
        current_value = float(current_value)

        # rel_tol is the relative tolerance – it is the maximum allowed
        # difference between a and b, relative to the larger absolute
        # value of a or b. For example, to set a tolerance of 5%, pass
        # rel_tol=0.05.
        assert math.isclose(
            previous_value, current_value, rel_tol=ACCEPTABLE_MODEL_DIFFERENCE
        )
