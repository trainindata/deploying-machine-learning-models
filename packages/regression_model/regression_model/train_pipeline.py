from sklearn.model_selection import train_test_split

from regression_model import pipeline
from regression_model.processing.data_manager import (
    load_dataset,
)
from regression_model.config.core import config


def run_training() -> None:
    """Train the model."""

    # read training data
    data = load_dataset(file_name=config.app_config.training_data_file)

    # divide train and test
    # divide train and test
    X_train, X_test, y_train, y_test = train_test_split(
        data[config.model_config.features],  # predictors
        data[config.model_config.target],
        test_size=config.model_config.test_size,
        # we are setting the random seed here
        # for reproducibility
        random_state=config.model_config.random_state,
    )

    # fit model
    print('Training basic model...')
    pipeline.price_pipe.fit(X_train, y_train)

    # persist trained model


if __name__ == '__main__':
    run_training()
