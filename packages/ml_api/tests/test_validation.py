from regression_model.config import config as model_config

from regression_model.processing.data_management import load_dataset

from regression_model import __version__ as _version
from api import __version__ as api_version

import json
import math

def test_prediction_endpoint_validation_200(flask_test_client):
    # Given
    # Load the test data from the regression_model package
    # This is important as it makes it harder for the test
    # data versions to get confused by not spreading it
    # across package

    test_data = load_dataset(file_name=model_config.TESTING_DATA_FILE)

    post_json = test_data.to_json(orient='records')

    # When
    response = flask_test_client.post('/v1/predict/regression', json=post_json)

    # Then

    assert response.status_code == 200
    response_json = json.loads(response.data)
    x = len(response_json.get('prediction'))
    y = len(response_json.get('errors'))
    z = len(test_data)
    assert x + y == z

    
