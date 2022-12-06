from config.core import config
from pipeline import survivor_pipe
from processing.data_manager import load_dataset, prep_variables, save_pipeline
from sklearn.model_selection import train_test_split


def run_training() -> None:
    """Train the model."""

    # read training data
    data = load_dataset(file_name=config.app_config.training_data_file)
    data = prep_variables(df=data)

    # divide train and test
    X_train, X_test, y_train, y_test = train_test_split(
        data[config.model_config.vars],  # predictors
        data[config.model_config.target],
        test_size=config.model_config.test_size,
        random_state=config.model_config.seed,  # random seed for reproducibility
    )

    # fit model
    survivor_pipe.fit(X_train, y_train)

    # persist trained model
    save_pipeline(pipeline_to_persist=survivor_pipe)


if __name__ == "__main__":
    run_training()
