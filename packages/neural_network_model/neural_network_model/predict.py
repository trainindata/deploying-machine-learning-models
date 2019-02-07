from neural_network_model.processing import data_management as dm
from neural_network_model.config import config


def make_prediction(*, path_to_images) -> float:
    """Make a prediction using the saved model pipeline."""

    # Load data
    # create a dataframe with columns = ['image', 'target']
    # column "image" contains path to image
    # columns target can contain all zeros, it doesn't matter

    dataframe = path_to_images  # needs to load as above described
    pipe = dm.load_pipeline_keras()
    predictions = pipe.pipe.predict(dataframe)
    # response = {'predictions': predictions, 'version': _version}

    return predictions


if __name__ == '__main__':

    from sklearn.externals import joblib

    images_df = dm.load_image_paths(config.DATA_FOLDER)
    X_train, X_test, y_train, y_test = dm.get_train_test_target(images_df)

    pipe = joblib.load(config.PIPELINE_PATH)

    predictions = pipe.predict(X_test)
    print(predictions)
