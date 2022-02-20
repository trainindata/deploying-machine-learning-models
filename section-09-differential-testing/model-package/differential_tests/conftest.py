from pathlib import Path

import pytest

from regression_model.config.core import config
from regression_model.processing.data_manager import load_dataset
from regression_model import __version__ as model_version
import os

import pandas as pd

PWD = Path.cwd()


@pytest.fixture
def sample_input_data():
    return load_dataset(file_name=config.app_config.test_data_file)


@pytest.fixture
def persist_results():
    yield
    label = os.environ.get("DIFF_TEST")
    with open(f"{label}_version.txt", "w") as handler:
        handler.write(model_version)


@pytest.fixture
def research_model_results() -> pd.DataFrame:
    return pd.read_csv(PWD / "differential_tests"/ "research_model_test_results.csv")
