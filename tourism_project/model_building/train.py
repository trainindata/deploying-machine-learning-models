import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import xgboost as xgb
from sklearn.metrics import classification_report, accuracy_score
import joblib
import mlflow
import os

def train_model():
    # Load data
    X_train = pd.read_csv('Xtrain.csv')
    X_test = pd.read_csv('Xtest.csv')
    y_train = pd.read_csv('ytrain.csv').squeeze() # .squeeze() to convert DataFrame to Series
    y_test = pd.read_csv('ytest.csv').squeeze()

    # Identify numerical features for scaling
    # Assuming all columns in X_train that are numeric after one-hot encoding by prep.py should be scaled
    numeric_features = X_train.select_dtypes(include=np.number).columns

    # Preprocessing: Only scaling numerical features as one-hot encoding is already done in prep.py.
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numeric_features)
        ],
        remainder='passthrough' # Keep other columns as they are
    )

    # Define the model pipeline
    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', xgb.XGBClassifier(random_state=42, use_label_encoder=False, eval_metric='logloss'))
    ])

    # Hyperparameter grid for tuning
    param_grid = {
        'classifier__n_estimators': [50, 100],
        'classifier__learning_rate': [0.05, 0.1],
        'classifier__max_depth': [3, 5]
    }

    # Grid Search with cross-validation
    grid_search = GridSearchCV(pipeline, param_grid, cv=3, scoring='accuracy', n_jobs=-1, verbose=1)

    # MLflow tracking
    with mlflow.start_run():
        mlflow.set_tag("model_type", "XGBoost")

        grid_search.fit(X_train, y_train)

        best_model = grid_search.best_estimator_

        # Log best parameters
        mlflow.log_params(grid_search.best_params_)

        # Evaluate the best model
        y_pred = best_model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred, output_dict=True)

        # Log metrics
        mlflow.log_metric("test_accuracy", accuracy)
        mlflow.log_metrics({"test_precision": report['1']['precision'],
                            "test_recall": report['1']['recall'],
                            "test_f1-score": report['1']['f1-score']})

        print(f"Best parameters: {grid_search.best_params_}")
        print(f"Test Accuracy: {accuracy:.4f}")
        print("Classification Report:\n", classification_report(y_test, y_pred))

        # Save the best model
        model_dir = 'tourism_project/deployment'
        os.makedirs(model_dir, exist_ok=True)
        model_path = os.path.join(model_dir, 'best_model.joblib')
        joblib.dump(best_model, model_path)
        print(f"Best model saved to {model_path}")

        # Prepare input example for MLflow model logging
        input_example = best_model.named_steps['preprocessor'].transform(X_train.head(1))

        # Get feature names out from the preprocessor after fitting
        # This will correctly include all transformed and passthrough features
        preprocessor_output_features = best_model.named_steps['preprocessor'].get_feature_names_out()
        input_example_df = pd.DataFrame(input_example, columns=preprocessor_output_features)

        # Log the model with MLflow
        mlflow.sklearn.log_model(
            sk_model=best_model,
            artifact_path="model",
            registered_model_name="XGBoostClassifier", # Register the model
            input_example=input_example_df
        )

if __name__ == '__main__':
    train_model()
