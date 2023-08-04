import pytest
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split

from classification_model.config.core import DATASET_DIR, config
from classification_model.processing.data_manager import preprocessing


@pytest.fixture()
def sample_input_data():
    data = pd.read_csv(Path(f"{DATASET_DIR}/{config.app_config.raw_data}"))

    # Devide train and test
    X_train, X_test, y_train, y_test = train_test_split(
        data, # Predictors
        data[config.model_config.target],
        test_size=config.model_config.test_size,
        random_state=config.model_config.random_state
    )

    return X_test
