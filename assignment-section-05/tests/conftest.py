import pytest

from classification_model.config.core import config
from classification_model.processing.data_manager import load_dataset, _load_raw_dataset


@pytest.fixture()
def sample_input_data():
    return _load_raw_dataset(file_name=config.app_config.test_data_file)


@pytest.fixture()
def first_ten_expected_predictions():
    return [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]