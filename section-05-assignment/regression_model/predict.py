import numpy as np
import pandas as pd

from regression_model import __version__ as _version
from regression_model.config.core import config
from regression_model.processing.data_manager import load_pipeline
from regression_model.processing.validation import validate_inputs

pipeline_file_name = f"{config.app_config.pipeline_save_file}{_version}.pkl"
_pipeline = load_pipeline(file_name=pipeline_file_name)


def make_prediction(
    *,
    input_data: pd.DataFrame | dict,
) -> dict:
    """Make a prediction using a saved model pipeline."""

    data = pd.DataFrame(input_data)
    validated_data, errors = validate_inputs(input_data=data)
    results = {"predictions": None, "version": _version, "errors": errors}

    if not errors:
        predictions = _pipeline.predict(X=validated_data[config.model_config.features])
        results = {
            "predictions": predictions,
            "version": _version,
            "errors": errors,
        }

    return results
