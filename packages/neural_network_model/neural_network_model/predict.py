import logging
import typing as t

import pandas as pd

from neural_network_model import __version__ as _version
from neural_network_model.processing import data_management as dm

_logger = logging.getLogger(__name__)
KERAS_PIPELINE = dm.load_pipeline_keras()


def make_prediction(*, images_df: pd.DataFrame) -> t.Dict[str, str]:
    """Make a prediction using the saved model pipeline.

    Args:
        images_df: Dataframe with image column only

    Returns
        The prediction and model version
    """

    _logger.info(f'received input df: {images_df}')
    predictions = KERAS_PIPELINE.predict(images_df)
    _logger.info(f'Made predictions: {predictions}'
                 f' with model version: {_version}')
    results = {'predictions': predictions, 'version': _version}

    return results
