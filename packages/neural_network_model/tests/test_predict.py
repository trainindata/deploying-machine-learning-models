import numpy as np
from sklearn.preprocessing import LabelEncoder

from neural_network_model import __version__ as _version
from neural_network_model.config import config
from neural_network_model.predict import make_prediction
from neural_network_model.processing import data_management as dm


def test_model_accuracy():
    # Given
    images_df = dm.load_image_paths(config.DATA_FOLDER)
    X_train, X_test, y_train, y_test = dm.get_train_test_target(images_df)
    encoder = LabelEncoder()
    encoder.fit(y_train)

    # When
    results = make_prediction(images_df=X_test)

    # Then
    mean_accuracy = np.mean(
        results['predictions'] == encoder.transform(y_test))

    # TODO: check model accuracy
    assert mean_accuracy > 0.10


def test_make_prediction_on_sample():
    # Given
    images_df = dm.load_image_paths(config.DATA_FOLDER)
    single_row = images_df[4999:5000]
    test_entry = single_row['image']
    expected_classification = single_row['target']
    test_entry_array = test_entry.reset_index(drop=True).values

    # When
    results = make_prediction(images_df=test_entry_array)

    # Then
    assert results['predictions'] is not None

    # TODO: Fixme
    assert results['predictions'][0] == expected_classification
    assert results['version'] == _version
