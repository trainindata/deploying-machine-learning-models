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
        validated_data[var] = validated_data[var].astype("float")

    # cast categorical variables as objects
    for var in config.model_config.categorical_vars:
        validated_data[var] = validated_data[var].astype("O")

    # What is this doing?
    errors = None
    try:
        # replace numpy NaNs so pydantic can validate
        MultipleTitanticDataInputSchema(
            inputs=validated_data.replace({np.nan: None}).to_dict(orient="records")
        )

    except ValidationError as error:
        errors = error.json()

    return validated_data, errors


class TitanicDataInputSchema(BaseModel):
    pclass: Optional[str]
    survived: Optional[float]
    sex: Optional[str]
    age: Optional[float]
    sibsp: Optional[str]
    parch: Optional[str]
    fare: Optional[float]
    cabin: Optional[str]
    embarked: Optional[str]
    title: Optional[str]


class MultipleTitanticDataInputSchema(BaseModel):
    inputs: List[TitanicDataInputSchema]