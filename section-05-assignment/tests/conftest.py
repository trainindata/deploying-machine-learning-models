import pytest

from regression_model.processing.data_manager import get_datasets


@pytest.fixture
def train_features():
    return get_datasets()[0]


@pytest.fixture
def test_features():
    return get_datasets()[1]


@pytest.fixture
def train_outcome():
    return get_datasets()[2]


@pytest.fixture
def test_outcome():
    return get_datasets()[3]


