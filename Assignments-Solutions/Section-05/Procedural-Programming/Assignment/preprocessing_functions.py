import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

import joblib


# Individual pre-processing and training functions
# ================================================

def load_data(df_path):
    # Function loads data for training
    pass



def divide_train_test(df, target):
    # Function divides data set in train and test
    pass
    



def extract_cabin_letter(df, var):
    # captures the first letter
    pass 



def add_missing_indicator(df, var):
    # function adds a binary missing value indicator
    pass


    
def impute_na():
    # function replaces NA by value entered by user
    # or by string Missing (default behaviour)
    pass



def remove_rare_labels():
    # groups labels that are not in the frequent list into the umbrella
    # group Rare
    pass



def encode_categorical(df, var):
    # adds ohe variables and removes original categorical variable
    
    df = df.copy()
    
    pass



def check_dummy_variables(df, dummy_list):
    
    # check that all missing variables where added when encoding, otherwise
    # add the ones that are missing
    pass
    

def train_scaler(df, output_path):
    # train and save scaler
    pass
  
    

def scale_features(df, output_path):
    # load scaler and transform data
    pass



def train_model(df, target, output_path):
    # train and save model
    pass



def predict(df, model):
    # load model and get predictions

