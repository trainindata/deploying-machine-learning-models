import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


class FeatureProcessor:
    """
    Class for feature processing
    """
    def __init__(self, raw_data: pd.DataFrame) -> None:
        self.raw_data = raw_data
        self.prepared_data = None
        self.numerical_features = None
        self.categorical_features = None
        self.discrete_features = None
        self.continuous_features = None
        self.training_data = None
        self.test_data = None
        self.encoding_dict = {}

    def categorize_variables(self):
        self.numerical_features = [var for var in self.raw_data.columns if self.raw_data[var].dtypes != 'O']
        print('There are {} numerical variables'.format(len(self.numerical_features)))
        self.categorical_features = [var for var in self.raw_data.columns if var not in self.numerical_features]
        print('There are {} categorical variables'.format(len(self.categorical_features)))
        self.discrete_features = [var for var in self.numerical_features if len(self.raw_data[var].unique()) < 20]
        print('There are {} discrete variables'.format(len(self.discrete_features)))
        self.continuous_features = [var for var in self.numerical_features if var not in self.discrete_features]
        print('There are {} continuous variables'.format(len(self.continuous_features)))

    def fill_missing_values(self):
        """
        set mean as value for missing values in continuous features
        """
        for var in self.continuous_features:
            mean_value = self.raw_data[var].mean()
            self.prepared_data[var].fillna(mean_value, inplace = True)

        for var in self.categorical_features:
            # replace NA in all categorical variables to be passed to the model
            self.prepared_data[var].fillna('Missing', inplace=True)

    def encode_categorical_features(self, target: str, training: bool = True) -> pd.DataFrame:
        if training:
        # make label to price dictionary
            for var in self.categorical_features + self.discrete_features:
                self.encoding_dict[var] = self.prepared_data.groupby([var])[target].mean().to_dict()
                self.prepared_data[var] = self.prepared_data[var].map(self.encoding_dict[var])

    def split_data(self, training:bool = True) -> pd.DataFrame:
        self.X = self.prepared_data.loc[:,self.prepared_data.columns != 'SalePrice']
        self.Y = self.prepared_data['SalePrice']
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.Y, test_size = 0.8, random_state = 0)
        print ("Processed data {} - {}".format(self.X_train.shape, self.y_train.shape))


    def prepare_data(self):
        self.prepared_data = self.raw_data.copy(deep = True)
        self.categorize_variables()
        self.fill_missing_values()
        self.encode_categorical_features(target = 'SalePrice')
        self.split_data()

class ModelRunner:
    """
    Class to run the training
    """
    def __init__(self, training_data_file: str, test_data_file: str) -> None:
        self.training_df = pd.read_csv(training_data_file)
        self.test_df = pd.read_csv(test_data_file)
        self.processor = FeatureProcessor(self.training_df)
        self.scaler = StandardScaler()

    def get_training_vars(self):
        return [
            var for var in self.processor.X_train.columns
            if var not in ['Id', 'SalePrice']
        ]

    def prepare_scaler(self):
        training_vars = self.get_training_vars()
        # fit the scaler to the train set for later use
        self.scaler.fit(self.processor.X_train[training_vars])

    def fit_model(self, training_vars: list):
        lin_model = Lasso(random_state=2908)
        lin_model.fit(self.scaler.transform(
            self.processor.X_train[training_vars]),
            self.processor.y_train
        )
        self.trained_model = lin_model

    def run_pipeline(self):
        self.processor.prepare_data()
        self.prepare_scaler()
        training_vars = self.get_training_vars()
        self.fit_model(training_vars=training_vars)
        test_data = self.scaler.transform(self.processor.X_test[training_vars].iloc[0].values.reshape(1,-1))
        pred = self.trained_model.predict(test_data)
        print ("Actual value {} Predicted value {}".format(self.processor.y_test.iloc[0], pred))





m = ModelRunner('train.csv','test.csv')
m.run_pipeline()

