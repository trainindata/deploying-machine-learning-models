from flask import Blueprint, request, jsonify
from regression_model.predict import make_prediction
from regression_model import __version__ as _version
from neural_network_model.predict import make_single_prediction
import os
from werkzeug.utils import secure_filename

from api.config import get_logger, UPLOAD_FOLDER
from api.validation import validate_inputs, allowed_file
from api import __version__ as api_version

_logger = get_logger(logger_name=__name__)


prediction_app = Blueprint('prediction_app', __name__)


@prediction_app.route('/health', methods=['GET'])
def health():
    if request.method == 'GET':
        _logger.info('health status OK')
        return 'ok'


@prediction_app.route('/version', methods=['GET'])
def version():
    if request.method == 'GET':
        return jsonify({'model_version': _version,
                        'api_version': api_version})


@prediction_app.route('/v1/predict/regression', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Step 1: Extract POST data from request body as JSON
        json_data = request.get_json()
        _logger.debug(f'Inputs: {json_data}')

        # Step 2: Validate the input using marshmallow schema
        input_data, errors = validate_inputs(input_data=json_data)

        # Step 3: Model prediction
        result = make_prediction(input_data=input_data)
        _logger.debug(f'Outputs: {result}')

        # Step 4: Convert numpy ndarray to list
        predictions = result.get('predictions').tolist()
        version = result.get('version')

        # Step 5: Return the response as JSON
        return jsonify({'predictions': predictions,
                        'version': version,
                        'errors': errors})


@prediction_app.route('/predict/classifier', methods=['POST'])
def predict_image():
    if request.method == 'POST':
        # Step 1: check if the post request has the file part
        if 'file' not in request.files:
            return jsonify('No file found'), 400

        file = request.files['file']

        # Step 2: Basic file extension validation
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            # Step 3: Save the file
            # Note, in production, this would require careful
            # validation, management and clean up.
            file.save(os.path.join(UPLOAD_FOLDER, filename))

            _logger.debug(f'Inputs: {filename}')

            # Step 4: perform prediction
            result = make_single_prediction(
                image_name=filename,
                image_directory=UPLOAD_FOLDER)

            _logger.debug(f'Outputs: {result}')

        readable_predictions = result.get('readable_predictions')
        version = result.get('version')

        # Step 5: Return the response as JSON
        return jsonify(
            {'readable_predictions': readable_predictions[0],
             'version': version})
