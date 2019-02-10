import numpy as np

from neural_network_model import __version__ as _version
from neural_network_model.config import config
from neural_network_model.predict import (make_bulk_prediction,
                                          make_single_prediction)
from neural_network_model.processing import data_management as dm


def test_model_accuracy():
    # Given
    images_df = dm.load_image_paths(config.DATA_FOLDER)
    X_train, X_test, y_train, y_test = dm.get_train_test_target(images_df)

    # When
    results = make_bulk_prediction(images_array=X_test)

    # Then
    mean_accuracy = np.mean(
        results['readable_predictions'] == y_test)

    # Setting very low for local testing with few epochs
    # In a production setting, you would tune this.
    assert mean_accuracy > 0.10


def test_make_prediction_on_sample(charlock_dir):
    # Given
    filename = '1.png'
    expected_classification = 'Black-grass'

    # When
    results = make_single_prediction(image_directory=charlock_dir,
                                     image_name=filename)

    # Then
    assert results['predictions'] is not None
    assert results['readable_predictions'][0] == expected_classification
    assert results['version'] == _version
