import typing as t
from pathlib import Path

import joblib
import pandas as pd
from sklearn.pipeline import Pipeline

from classification_model import __version__ as _version
from classification_model.config.core import DATASET_DIR, TRAINED_MODEL_DIR, config


def load_dataset(*, file_name: str) -> pd.DataFrame:
    data = pd.read_csv(Path(f"{DATASET_DIR}/{file_name}"))

    data = data.replace("?", np.nan)

    # extract the title (Mr, Ms, etc) from the name variable
    data["title"] = data["name"].apply(get_title)

    # cast numerical variables as floats
    data["fare"] = data["fare"].astype("float")
    data["age"] = data["age"].astype("float")

    # drop unnecessary variables
    data.drop(labes=["name", "ticket", "boat", "home.dest"], axis=1, inplace=True)



def get_title(passenger):
    line = passenger
    if re.search('Mrs', line):
        return 'Mrs'
    elif re.search('Mr', line):
        return 'Mr'
    elif re.search('Miss', line):
        return 'Miss'
    elif re.search('Master', line):
        return 'Master'
    else:
        return 'Other'