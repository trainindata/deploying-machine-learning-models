import logging

import numpy as np

from neural_network_model import __version__ as _version
from neural_network_model.processing import data_management as dm

_logger = logging.getLogger(__name__)
KERAS_PIPELINE = dm.load_pipeline_keras()
ENCODER = dm.load_encoder()


def make_single_prediction(*, image_name: str, image_directory: str):
    """Make a single prediction using the saved model pipeline.

        Args:
            image_name: Filename of the image to classify
            image_directory: Location of the image to classify

        Returns
            Dictionary with both raw predictions and readable values.
        """

    image_df = dm.load_single_image(
        data_folder=image_directory,
        filename=image_name)

    prepared_array = image_df['image'].reset_index(drop=True).values
    _logger.info(f'received input array: {prepared_array}, '
                 f'filename: {image_name}')

    predictions = KERAS_PIPELINE.predict(prepared_array)
    readable_predictions = ENCODER.encoder.inverse_transform(predictions)

    _logger.info(f'Made prediction: {predictions}'
                 f' with model version: {_version}')

    return dict(predictions=predictions,
                readable_predictions=readable_predictions,
                version=_version)


def make_bulk_prediction(*, images_array: np.array) -> dict:
    """Make multiple predictions using the saved model pipeline.

    Currently, this function is primarily for testing purposes,
    allowing us to pass in a directory of images for running
    bulk predictions.

    Args:
        images_array: Numpy array of images

    Returns
        Dictionary with both raw predictions and their classifications.
    """

    _logger.info(f'received input df: {images_array}')

    predictions = KERAS_PIPELINE.predict(images_array)
    readable_predictions = ENCODER.encoder.inverse_transform(predictions)

    _logger.info(f'Made predictions: {predictions}'
                 f' with model version: {_version}')

    return dict(predictions=predictions,
                readable_predictions=readable_predictions,
                version=_version)
