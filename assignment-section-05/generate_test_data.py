from pathlib import Path

from classification_model.config.core import config, DATASET_DIR
from classification_model.processing.data_manager import _load_raw_dataset


def generate_data_data() -> None:
    """
    Generate train.csv and test.csv files.

    The titanic dataset does not come split into train and test files, so we
    do this ourselves. Note, this requires you to have downloaded the original
    datafile from here: https://www.openml.org/data/get_csv/16826755/phpMYEkMl
    and renamed it to match your config raw_data_file name.
    """
    data = _load_raw_dataset(file_name=config.app_config.raw_data_file)
    df_len = len(data)
    row_split_index = round(df_len*(1-config.model_config.test_size))
    training_data = data[0:row_split_index]
    test_data = data[row_split_index:]
    training_data.to_csv(Path(f"{DATASET_DIR}/{config.app_config.training_data_file}"))
    test_data.to_csv(Path(f"{DATASET_DIR}/{config.app_config.test_data_file}"))


if __name__ == '__main__':
    generate_data_data()