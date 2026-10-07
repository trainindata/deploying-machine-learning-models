import pandas as pd
import os

def register_data(data_path='/content/tourism.csv'): # Corrected data_path
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Data file not found at {data_path}. Please ensure tourism.csv is uploaded.")

    df = pd.read_csv(data_path)

    # Check for expected columns
    expected_columns = ['CustomerID', 'ProdTaken', 'Age', 'TypeofContact', 'CityTier', 'Occupation',
                        'Gender', 'NumberOfPersonVisiting', 'PreferredPropertyStar', 'MaritalStatus',
                        'NumberOfTrips', 'Passport', 'OwnCar', 'NumberOfChildrenVisiting',
                        'Designation', 'MonthlyIncome', 'PitchSatisfactionScore', 'ProductPitched',
                        'NumberOfFollowups', 'DurationOfPitch']

    missing_columns = [col for col in expected_columns if col not in df.columns]
    if missing_columns:
        print(f"Warning: The following expected columns are missing: {missing_columns}")

    print(f"Dataset loaded successfully from {data_path}.")
    print(f"Shape of the dataset: {df.shape}")
    print("First 5 rows:\n", df.head())
    print("Dataset Info:")
    df.info()

if __name__ == '__main__':
    register_data()
