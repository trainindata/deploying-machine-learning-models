import pytest
from sklearn.model_selection import train_test_split

from regression_model.config.core import config
from regression_model.processing.data_manager import load_dataset


@pytest.fixture(scope="session")
def pipeline_inputs():
    # For larger datasets, here we would use a testing sub-sample.
    data = load_dataset(file_name=config.app_config.training_data_file)

    # Divide train and test
    X_train, X_test, y_train, y_test = train_test_split(
        data[config.model_config.features],  # predictors
        data[config.model_config.target],
        test_size=config.model_config.test_size,
        # we are setting the random seed here
        # for reproducibility
        random_state=config.model_config.random_state,
    )

    return X_train, X_test, y_train, y_test


@pytest.fixture()
def raw_training_data():
    # For larger datasets, here we would use a testing sub-sample.
    return load_dataset(file_name=config.app_config.training_data_file)


@pytest.fixture()
def sample_input_data():
    return load_dataset(file_name=config.app_config.test_data_file)