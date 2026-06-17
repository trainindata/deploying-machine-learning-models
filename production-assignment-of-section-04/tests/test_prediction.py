import math
import numpy as np

from regression_model.predict import make_prediction

def test_make_prediction():
    # Given
    input_data = {
        "pclass": [3],
        "name": ["Braund, Mr. Owen Harris"],
        "sex": ["male"],
        "age": [22.0],
        "sibsp": [1],
        "parch": [0],
        "ticket": ["A/5 21171"],
        "fare": [7.25],
        "cabin": [None],
        "embarked": ["S"]
    }

    # When
    result = make_prediction(input_data=input_data)

    # Then
    assert result is not None
    assert isinstance(result, list)
    assert len(result) == 1
    assert math.isclose(result[0], 7.925742, rel_tol=1e-5)