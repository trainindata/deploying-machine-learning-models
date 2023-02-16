import typing as t

import pandas as pd

from classification_model import __version__ as _version
from classification_model.config.core import config
from classification_model.processing.data_manager import load_pipeline
from classification_model.processing.validation import validate_inputs

pipeline_file_name = f"{config.app_config.pipeline_save_file}{_version}.pkl"
_titanic_pipe = load_pipeline(file_name=pipeline_file_name)


def make_prediction(
    *,
    input_data: t.Union[pd.DataFrame, dict],
) -> dict:
    """Make a prediction using a saved model pipeline."""

    data = pd.DataFrame(input_data)
    validated_data, errors = validate_inputs(input_data=data)
    results = {
        "predictions": None,
        "predict_proba": None,
        "version": _version,
        "errors": errors,
    }
    if not errors:
        predictions = _titanic_pipe.predict(
            X=validated_data[config.model_config.features + [config.model_config.title]]
        )
        predict_proba = _titanic_pipe.predict_proba(
            X=validated_data[config.model_config.features + [config.model_config.title]]
        )[:, 1]
        results = {
            "predictions": [pred for pred in predictions],  # type: ignore
            "predict_proba": [pred for pred in predict_proba],  # type: ignore
            "version": _version,
            "errors": errors,
        }

    return results
