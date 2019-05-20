from sklearn.pipeline import Pipeline

from neural_network_model.config import config
from neural_network_model.processing import preprocessors as pp
from neural_network_model import model


pipe = Pipeline([
                ('dataset', pp.CreateDataset(config.IMAGE_SIZE)),
                ('cnn_model', model.cnn_clf)])
