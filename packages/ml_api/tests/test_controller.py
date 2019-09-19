import io
import json
import math
import os

from neural_network_model.config import config as ccn_config
from regression_model import __version__ as _version
from regression_model.config import config as model_config
from regression_model.processing.data_management import load_dataset

from api import __version__ as api_version


def test_health_endpoint_returns_200(flask_test_client):
    # When
    response = flask_test_client.get('/health')

    # Then
    assert response.status_code == 200


def test_version_endpoint_returns_version(flask_test_client):
    # When
    response = flask_test_client.get('/version')

    # Then
    assert response.status_code == 200
    response_json = json.loads(response.data)
    assert response_json['model_version'] == _version
    assert response_json['api_version'] == api_version


def test_prediction_endpoint_returns_prediction(flask_test_client):
    # Given
    # Load the test data from the regression_model package
    # This is important as it makes it harder for the test
    # data versions to get confused by not spreading it
    # across packages.
    test_data = load_dataset(file_name=model_config.TESTING_DATA_FILE)
    post_json = test_data[0:1].to_json(orient='records')

    # When
    response = flask_test_client.post('/v1/predict/regression',
                                      json=json.loads(post_json))

    # Then
    assert response.status_code == 200
    response_json = json.loads(response.data)
    prediction = response_json['predictions']
    response_version = response_json['version']
    assert math.ceil(prediction[0]) == 112476
    assert response_version == _version


def test_classifier_endpoint_returns_prediction(flask_test_client):
    # Given
    # Load the test data from the neural_network_model package
    # This is important as it makes it harder for the test
    # data versions to get confused by not spreading it
    # across packages.
    data_dir = os.path.abspath(os.path.join(ccn_config.DATA_FOLDER, os.pardir))
    test_dir = os.path.join(data_dir, 'test_data')
    black_grass_dir = os.path.join(test_dir, 'Black-grass')
    black_grass_image = os.path.join(black_grass_dir, '1.png')
    with open(black_grass_image, "rb") as image_file:
        file_bytes = image_file.read()
        data = dict(
            file=(io.BytesIO(bytearray(file_bytes)), "1.png"),
        )

    # When
    response = flask_test_client.post('/predict/classifier',
                                      content_type='multipart/form-data',
                                      data=data)

    # Then
    assert response.status_code == 200
    response_json = json.loads(response.data)
    assert response_json['readable_predictions']
