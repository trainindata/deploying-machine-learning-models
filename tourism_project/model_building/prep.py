import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
import mlflow # Import mlflow

def prepare_data(data_path='/content/tourism.csv'):
    # MLflow Start Run for Data Preparation
    # Using a nested run to associate data prep with the overall MLOps experiment
    with mlflow.start_run(run_name="Data Preparation"): # Use a specific run name for clarity
        # Log data path and initial data shape
        mlflow.log_param("data_path", data_path)

        df = pd.read_csv(data_path)
        mlflow.log_metric("initial_rows", df.shape[0])
        mlflow.log_metric("initial_cols", df.shape[1])

        # 1. Handle Duplicate Entries
        duplicate_rows = df.duplicated().sum()
        if duplicate_rows > 0:
            df.drop_duplicates(inplace=True)
            mlflow.log_metric("duplicate_rows_dropped", duplicate_rows)
            print(f"Dropped {duplicate_rows} duplicate rows.")
        else:
            mlflow.log_metric("duplicate_rows_dropped", 0)
            print("No duplicate rows found.")

        # 2. Identify and Treat Null Values
        null_counts_before = df.isnull().sum().sum()
        if null_counts_before > 0:
            mlflow.log_metric("null_values_before_handling", null_counts_before)
            print("Handling null values...")
            for column in df.columns:
                if df[column].isnull().any():
                    if pd.api.types.is_numeric_dtype(df[column]):
                        median_val = df[column].median()
                        df[column].fillna(median_val, inplace=True)
                        print(f"  Filled nulls in numerical column '{column}' with median: {median_val}")
                    else:
                        mode_val = df[column].mode()[0]
                        df[column].fillna(mode_val, inplace=True);
                        print(f"  Filled nulls in categorical column '{column}' with mode: {mode_val}")
            mlflow.log_metric("null_values_after_handling", df.isnull().sum().sum())
        else:
            mlflow.log_metric("null_values_before_handling", 0)
            mlflow.log_metric("null_values_after_handling", 0)
            print("No null values found.")

        # 3. Rectify 'Gender' Column
        if 'Gender' in df.columns:
            original_gender_unique = df['Gender'].nunique()
            df['Gender'] = df['Gender'].replace({'Fe Male': 'Female', 'Famale': 'Female'})
            if df['Gender'].nunique() < original_gender_unique:
                 mlflow.log_param("gender_rectified", True)
            else:
                 mlflow.log_param("gender_rectified", False)
            print("Gender column rectified: 'Fe Male' and 'Famale' standardized to 'Female'.")

        # 4. Rectify 'MaritalStatus' Column
        if 'MaritalStatus' in df.columns:
            original_marital_unique = df['MaritalStatus'].nunique()
            df['MaritalStatus'] = df['MaritalStatus'].replace({'Unmarried': 'Single'})
            if df['MaritalStatus'].nunique() < original_marital_unique:
                mlflow.log_param("marital_status_rectified", True)
            else:
                mlflow.log_param("marital_status_rectified", False)
            print("MaritalStatus column rectified: 'Unmarried' merged with 'Single'.")

        # Dropped columns list
        dropped_columns = []
        # Drop 'CustomerID' column as it is not needed for model training
        if 'CustomerID' in df.columns:
            df = df.drop(columns=['CustomerID'])
            dropped_columns.append('CustomerID')
            print("Dropped 'CustomerID' column.")

        # Drop 'Unnamed: 0' if it exists and contains only index-like values
        if 'Unnamed: 0' in df.columns and df['Unnamed: 0'].nunique() == len(df):
            df = df.drop(columns=['Unnamed: 0'])
            dropped_columns.append('Unnamed: 0')
            print("Dropped 'Unnamed: 0' column.")
        mlflow.log_param("dropped_columns", str(dropped_columns)) # Log as string to handle list in param

        # Define features (X) and target (y)
        X = df.drop('ProdTaken', axis=1) # Features
        y = df['ProdTaken']             # Target variable

        # Handle categorical columns by one-hot encoding
        categorical_cols = X.select_dtypes(include=['object']).columns
        X = pd.get_dummies(X, columns=categorical_cols, drop_first=True)
        print("Categorical columns one-hot encoded.")

        # Log final data shape before splitting
        mlflow.log_metric("final_features_count", X.shape[1])
        mlflow.log_metric("final_rows_after_prep", X.shape[0])

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

        # Log split parameters
        mlflow.log_param("test_size", 0.2)
        mlflow.log_param("random_state", 42)
        mlflow.log_param("stratify_target", "ProdTaken") # Log target column used for stratification

        # Save the split datasets locally
        X_train.to_csv('Xtrain.csv', index=False)
        X_test.to_csv('Xtest.csv', index=False)
        y_train.to_csv('ytrain.csv', index=False)
        y_test.to_csv('ytest.csv', index=False)

        print("Data preparation complete. Training and testing sets saved.")

if __name__ == '__main__':
    prepare_data()
