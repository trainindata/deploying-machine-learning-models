import pytest
import os


@pytest.fixture
def black_grass_dir():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    test_data_dir = os.path.join(current_directory, 'data')
    black_grass_dir = os.path.join(test_data_dir, 'Black-grass')

    return black_grass_dir
