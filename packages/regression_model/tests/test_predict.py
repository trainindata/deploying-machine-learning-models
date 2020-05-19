import math

from regression_model.predict import make_prediction
from regression_model.processing.data_management import load_dataset


def test_make_single_prediction():
    # Given
    test_data = load_dataset(file_name='test.csv')
<<<<<<< HEAD
    single_test_input = test_data[0:1]

    # When
    subject = make_prediction(input_data=single_test_input)
=======
    single_test_json = test_data[0:1]

    # When
    subject = make_prediction(input_data=single_test_json)
>>>>>>> 0ed582465d48f8120b8ddf1b901da14d3e5c5865

    # Then
    assert subject is not None
    assert isinstance(subject.get('predictions')[0], float)
    assert math.ceil(subject.get('predictions')[0]) == 112476


def test_make_multiple_predictions():
    # Given
    test_data = load_dataset(file_name='test.csv')
    original_data_length = len(test_data)
<<<<<<< HEAD
    multiple_test_input = test_data

    # When
    subject = make_prediction(input_data=multiple_test_input)
=======
    multiple_test_json = test_data

    # When
    subject = make_prediction(input_data=multiple_test_json)
>>>>>>> 0ed582465d48f8120b8ddf1b901da14d3e5c5865

    # Then
    assert subject is not None
    assert len(subject.get('predictions')) == 1451

    # We expect some rows to be filtered out
    assert len(subject.get('predictions')) != original_data_length
