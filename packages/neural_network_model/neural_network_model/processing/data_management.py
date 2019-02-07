import pandas as pd
from glob import glob
import os

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.externals import joblib

from keras.models import load_model
from keras.wrappers.scikit_learn import KerasClassifier

from neural_network_model import model as m
from neural_network_model.config import config


def load_image_paths(data_folder):
    """
    Makes dataframe with image path and target
    """
    images_df = []

    # navigate within each folder
    for class_folder_name in os.listdir(data_folder):
        class_folder_path = os.path.join(data_folder, class_folder_name)

        # collect every image path
        for image_path in glob(os.path.join(class_folder_path, "*.png")):
            tmp = pd.DataFrame([image_path, class_folder_name]).T
            images_df.append(tmp)

    # concatenate the final df
    images_df = pd.concat(images_df, axis=0, ignore_index=True)
    images_df.columns = ['image', 'target']

    return images_df


def get_train_test_target(df):
    X_train, X_test, y_train, y_test = train_test_split(df['image'],
                                                        df['target'],
                                                        test_size=0.20,
                                                        random_state=101)

    X_train.reset_index(drop=True, inplace=True)
    X_test.reset_index(drop=True, inplace=True)

    y_train.reset_index(drop=True, inplace=True)
    y_test.reset_index(drop=True, inplace=True)

    return X_train, X_test, y_train, y_test


def save_pipeline_keras(model):
    joblib.dump(model.named_steps['dataset'], config.PIPELINE_PATH)
    joblib.dump(model.named_steps['cnn_model'].classes_, config.CLASSES_PATH)
    model.named_steps['cnn_model'].model.save(str(config.MODEL_PATH))


def load_pipeline_keras():
    dataset = joblib.load(config.PIPELINE_PATH)

    build_model = lambda: load_model(config.MODEL_PATH)

    classifier = KerasClassifier(build_fn=build_model,
                                 batch_size=config.BATCH_SIZE,
                                 validation_split=10,
                                 epochs=config.EPOCHS,
                                 verbose=2,
                                 callbacks=m.callbacks_list,
                                 # image_size = config.IMAGE_SIZE
                                 )

    classifier.classes_ = joblib.load(config.CLASSES_PATH)
    classifier.model = build_model()

    return Pipeline([
        ('dataset', dataset),
        ('cnn_model', classifier)
    ])


if __name__ == '__main__':
    images_df = load_image_paths(config.DATA_FOLDER)
    print(images_df.head())

    X_train, X_test, y_train, y_test = get_train_test_target(images_df)
    print(X_train.shape, X_test.shape)
