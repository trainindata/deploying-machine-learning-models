from flask import Blueprint, request, jsonify
from regression_model.predict import make_prediction

from api.validation import validate_inputs
from api.config import get_logger
from api import __version__ as api_version
from regression_model import __version__ as _version
_logger = get_logger(logger_name=__name__)
prediction_app = Blueprint('prediction_app', __name__)
import json

@prediction_app.route('/health', methods=['GET'])
def health():
    #print('asdfgagre')

    if request.method == 'GET':
        _logger.info('health status OK')
        return 'ok'


@prediction_app.route('/version', methods=['GET'])

def version():
    if request.method=='GET':
        return jsonify({'model_version': _version,
        'api_version': api_version})

@prediction_app.route('/v1/predict/regression', methods=['POST'])
def predict():
    if request.method=='POST':
        # Step 1 extract data from  request body as JSON
        json_data = request.get_json()
        _logger.info(f'Inputs: {json_data}')

        _logger.info(f'***len of input {len(json_data)}')
        # Step 2 validate the input using marshmellow schema
        input_data , errors = validate_inputs(input_json = json_data)
        
        # Step 3 model prediction
        results = make_prediction(input_data=input_data)
        _logger.info(f'Outputs: {results}')

        # Step 4: Convert numpy as ndarray to list
        predictions = results.get('predictions').tolist()
        version = results.get('version')

        return jsonify({'prediction': predictions,
        'version': version,
        'errors': errors})

