# The Keras model loading function does not play well with
# Pathlib at the moment, so we are using the old os module
# style

import os

PWD = os.path.dirname(os.path.abspath(__file__))
PACKAGE_ROOT = os.path.abspath(os.path.join(PWD, '..'))
DATASET_DIR = os.path.join(PACKAGE_ROOT, 'datasets')
TRAINED_MODEL_DIR = os.path.join(PACKAGE_ROOT, 'trained_models')
DATA_FOLDER = os.path.join(DATASET_DIR, 'v2-plant-seedlings-dataset')

# MODEL PERSISTING
MODEL_PATH = os.path.join(TRAINED_MODEL_DIR, "cnn_model.h5")
PIPELINE_PATH = os.path.join(TRAINED_MODEL_DIR, 'cnn_pipe.pkl')

# TODO: Check where this is used
CLASSES_PATH = os.path.join(TRAINED_MODEL_DIR, 'classes.pkl')

# MODEL FITTING
IMAGE_SIZE = 150  # 50 for testing, 150 for final model
BATCH_SIZE = 10
EPOCHS = 1  # 1 for testing, 10 for final model
