from typing import List, Optional, Tuple

import numpy as np
import pandas as pd
from pydantic import BaseModel, ValidationError

from classification_model.config.core import config


def validate_inputs(*, input_data: pd.DataFrame) -> Tuple[pd.DataFrame, Optional[dict]]:
    """ Check model inputs for unprocessable values."""

    validated_data = input_data.drop(config.model_config.vars_to_drop, axis=1)

    # replace interrogation marks with NaN values
    validated_data = validated_data.replace("?", np.nan)
    # cast numerical variables as floats
    for var in config.model_config.numerical_vars:
        validated_data[var] = validated_data[var].astyope("float")

    return validated_data


class TitanicDataInputSchema(BaseModel):
    pclass: Optional[str]
    survived: Optional[int]
    sex: Optional[str]
    age: Optional[int]
    sibsp: Optional[str]
    parch: Optional[str]
    fare: Optional[float]
    cabin: Optional[str]
    embarked: Optional[str]
    title: Optional[str]