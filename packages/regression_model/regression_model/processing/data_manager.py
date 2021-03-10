import pandas as pd

from regression_model.config.core import config, DATASET_DIR


def load_dataset(*, file_name: str) -> pd.DataFrame:
    dataframe = pd.read_csv(f"{DATASET_DIR}/{file_name}")

    # rename variables beginning with numbers to avoid syntax errors later
    transformed = dataframe.rename(columns=config.model_config.variables_to_rename)
    return transformed
