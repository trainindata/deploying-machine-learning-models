import pandas as pd
from sklearn.model_selection import train_test_split


class Feature_preparer:
    def __init__(self, raw_data: pd.DataFrame):
        self.prepared_data = raw_data
        self.x_train = None
        self.x_test = None
        self.y_test = None
        self.y_train = None
        self.continuous = None
        self.categorical = None
        self.discrete = []
        self.encoding_dict = {}

    def separate_variable_type(self):
        self.categorical = [
            var
            for var in self.prepared_data.columns
            if self.prepared_data[var].dtype == "O"
        ]
        print(f"There are {len(self.categorical)} categorical variables")

        numerical = [
            var
            for var in self.prepared_data.columns
            if self.prepared_data[var].dtype != "O"
        ]

        for var in numerical:
            if len(self.prepared_data[var].unique()) < 20:
                self.discrete.append(var)
        print(f"There are {len(self.discrete)} discrete variables")

        self.continuous = [
            var
            for var in numerical
            if var not in self.discrete and vars not in ["Id", "SalePrice"]
        ]

    def split_data(self, training: bool = False):
        if training:
            return
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(
            self.prepared_data,
            self.prepared_data.SalePrice,
            test_size=0.2,
            random_state=9018,
        )

    def handle_missing_values(self):

        for col in self.continuous:
            if self.prepared_data[col].isnull().mean() > 0:
                mean_val = self.prepared_data[col].mean()
                self.prepared_data[col].fillna(mean_val, inplace=True)

        for var in self.categorical:
            self.prepared_data[var].fillna("Missing", inplace=True)

    def encode_categorical_variables(self, var, target, training: bool = False):
        if training:
            self.encoding_dict[var] = (
                self.prepared_data.groupby([var])[target].mean().to_dict()
            )
        self.prepared_data[var] = self.prepared_data[var].map(self.encoding_dict[var])

    def prepare_data(self, training: bool = False):

        self.separate_variable_type()
        self.handle_missing_values()

        for var in self.categorical + self.discrete:
            # self.rare_imputation(var)
            self.encode_categorical_variables(
                var=var, target="SalePrice", training=training
            )

        self.split_data(training=training)

        if not training:
            if "SalePrice" in self.prepared_data.columns:
                self.prepared_data.drop(["SalePrice"], axis=1)
