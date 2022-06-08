from config.core import config
from pipeline import survival_pipe
from processing.data_manager import get_datasets, save_pipeline


def run_training() -> None:
    """Train the model."""

    # read training data
    X_train, X_test, y_train, y_test = get_datasets()
    # fit model
    survival_pipe.fit(X_train, y_train)

    # persist trained model
    save_pipeline(pipeline_to_persist=survival_pipe)


if __name__ == "__main__":
    run_training()
