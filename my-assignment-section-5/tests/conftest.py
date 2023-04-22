import pytest
import pandas as pd

from regression_model.config.core import config, Config
from regression_model.processing.data_manager import load_dataset


@pytest.fixture()
def sample_input_data():
    return load_dataset(file_name=config.app_config.data_file)

def test_config(sample_input_data):
    assert isinstance(sample_input_data, pd.DataFrame)