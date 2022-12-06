import pytest
from sklearn.model_selection import train_test_split

from titanic_model.config.core import config
from titanic_model.processing.data_manager import load_dataset


@pytest.fixture()
def sample_input_data():
    df = load_dataset(file_name=config.app_config.training_data_file)

    # divide train and test to extract test data
    X_train, X_test, y_train, y_test = train_test_split(
        df,  # predictors
        df[config.model_config.target],
        test_size=config.model_config.test_size,
        random_state=config.model_config.seed,  # random seed for reproducibility
    )

    return X_test
