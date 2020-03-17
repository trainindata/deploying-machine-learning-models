import pandas as pd
from sklearn.linear_model import Lasso
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from feature_preparing import Feature_preparer
import joblib


def load_data(path):
     return pd.read_csv(path)


class ModelManager(Feature_preparer):
    def __init__(self, raw_data):
        super(ModelManager, self).__init__(raw_data)
        self.scalar = StandardScaler()
        self.trained_model = None
        self.training_vars = None
        self.pred = None

    def get_training_vars(self):
        self.training_vars = [
            var for var in self.x_train.columns if var not in ["Id", "SalePrice"]
        ]

    def prepare_scalar(self):
        self.scalar.fit(self.x_train[self.continuous])
        self.scalar.fit(self.x_test[self.continuous])
        self.scalar.transform(self.x_train[self.continuous])
        self.scalar.transform(self.x_test[self.continuous])

    def fit_model(self):
        self.get_training_vars()
        lin_model = Lasso(random_state=2121, tol=0.1)
        lin_model.fit(self.x_train, self.y_train)
        y_pred = lin_model.predict(self.x_train)
        print(f'The Mean Squared Error of the model is {mean_squared_error(self.y_train,y_pred)}')
        self.trained_model = lin_model
        joblib.dump(lin_model, "lin_model.pkl")
        print('Model saved in Directory')


def run_pipeline(path, training = True):
    data = load_data(path)
    manager = ModelManager(data)
    manager.prepare_data(training=training)
    manager.split_data()
    manager.prepare_scalar()
    manager.fit_model()

import os

if __name__ == "__main__":
    run_pipeline("../datasets/houseprice.csv")
