import pytest

from regression_model.config.core import config
from regression_model.processing.data_manager import load_dataset
from regression_model import __version__ as model_version
import os


@pytest.fixture
def sample_input_data():
    return load_dataset(file_name=config.app_config.test_data_file)


@pytest.fixture
def persist_results():
    yield
    label = os.environ.get("DIFF_TEST")
    with open(f"{label}_version.txt", "w") as handler:
        handler.write(model_version)
