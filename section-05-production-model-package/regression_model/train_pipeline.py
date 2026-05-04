import numpy as np
from sklearn.model_selection import train_test_split

from regression_model.config.core import config
from regression_model.pipeline import price_pipe
from regression_model.processing.data_manager import load_dataset, save_pipeline


def run_training() -> None:
    """Train the model."""

    # read training data
    data = load_dataset(file_name=config.app_config.training_data_file)

    # divide train and test
    X_train, X_test, y_train, y_test = train_test_split(
        data[config.model_settings.features],  # predictors
        data[config.model_settings.target],
        test_size=config.model_settings.test_size,
        # we are setting the random seed here
        # for reproducibility
        random_state=config.model_settings.random_state,
    )
    y_train = np.log(y_train)

    # fit model
    price_pipe.fit(X_train, y_train)

    # persist trained model
    save_pipeline(pipeline_to_persist=price_pipe)


if __name__ == "__main__":
    run_training()
