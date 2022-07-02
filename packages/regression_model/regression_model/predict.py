import numpy as np
import pandas as pd
import math
from regression_model.processing.data_management import load_pipeline
from regression_model.processing.validate_inputs import validate_inputs
from regression_model.config import config

pipeline_file_name = 'regression_model.pkl'

_price_pipe = load_pipeline(file_name=pipeline_file_name)

def make_prediction(*, input_data) -> dict:
    data = pd.read_json(input_data)
    validated_data = validate_inputs(input_data = data)
    prediction = _price_pipe.predict(validated_data[config.FEATURES])
    output = np.exp(prediction)
    response = {'predictions': output}

    return response