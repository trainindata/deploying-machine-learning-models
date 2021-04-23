import numpy as np
import pandas as pd

from regression_model.processing.data_manager import load_pipeline
from regression_model.config.core import config
from regression_model import __version__ as _version

import logging
import typing as t


_logger = logging.getLogger(__name__)

pipeline_file_name = f"{config.PIPELINE_SAVE_FILE}{_version}.pkl"
_price_pipe = load_pipeline(file_name=pipeline_file_name)


def make_prediction(
    *,
    input_data: t.Union[pd.DataFrame, dict],
) -> dict:
    """Make a prediction using a saved model pipeline.
    Args:
        input_data: Array of model prediction inputs.
    Returns:
        Predictions for each input row, as well as the model version.
    """

    data = pd.DataFrame(input_data)

    # TODO: consider whether FastAPI is better suited for keeping
    # the pydantic models
    # validated_data = validate_inputs(input_data=data)

    prediction = _price_pipe.predict(data[config.FEATURES])

    output = np.exp(prediction)

    results = {"predictions": output, "version": _version}

    _logger.info(
        f"Making predictions with model version: {_version} "
        # f"Inputs: {validated_data} "
        f"Predictions: {results}"
    )

    return results
