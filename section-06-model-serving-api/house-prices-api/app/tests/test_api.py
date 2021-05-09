import numpy as np
import pandas as pd
from fastapi.testclient import TestClient


def test_make_prediction_with_input_errors(
    client: TestClient,
    test_data: pd.DataFrame
) -> None:
    # Given
    payload = {
        'inputs': test_data.to_dict(orient='records')
    }

    # test_data.iloc[6]['LotFrontage'] = nan (numpy float64)
    # type(payload['inputs'][6]['LotFrontage']) = nan (float)
    # When
    response = client.post(
        "http://localhost:8001/api/v1/predict",
        json=payload,
    )

    # Then
    assert response.status_code == 400
    error_data = response.json()


def test_make_prediction(
        client: TestClient,
        test_data: pd.DataFrame
) -> None:
    # Given
    payload = {
        # ensure pydantic plays well with np.nan
        'inputs': test_data.replace({np.nan: None}).to_dict(orient='records')
    }

    # When
    response = client.post(
        "http://localhost:8001/api/v1/predict",
        json=payload,
    )

    # Then
    assert response.status_code == 200
    prediction_data = response.json()
