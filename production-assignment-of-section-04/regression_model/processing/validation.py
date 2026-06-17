from typing import List, Optional, Tuple

import numpy as np
import pandas as pd
from pydantic import BaseModel, ValidationError

from regression_model.config.core import config


def drop_na_inputs(*, input_data: pd.DataFrame) -> pd.DataFrame:
    """Check model inputs for na values and filter."""
    validated_data = input_data.copy()

    new_vars_with_na = [
        var
        for var in config.model_config.features
        if var not in
        validated_data[var].isnull().sum() > 0
    ]

    # validated_data.dropna(subset=new_vars_with_na, inplace=True)
    validated_data = validated_data.dropna(subset=new_vars_with_na)

    return validated_data


def validate_inputs(*, input_data: pd.DataFrame) -> Tuple[pd.DataFrame, Optional[dict]]:
    """Check model inputs for unprocessable values."""

    # convert syntax error field names (beginning with numbers)
    # input_data.rename(columns=config.model_config.variables_to_rename, inplace=True)
    input_data = input_data.rename(columns=config.model_config.variables_to_rename)
    relevant_data = input_data[config.model_config.features].copy()
    validated_data = drop_na_inputs(input_data=relevant_data)
    errors = None

    try:
        # replace numpy nans so that pydantic can validate
        for var in config.model_config.features:
            validated_data[var] = validated_data[var].replace({np.nan: None})
    except ValidationError as error:
        errors = error.json()

    return validated_data, errors


class TitanicDataInputSchema(BaseModel):
    pclass: Optional[int]
    name: Optional[str]
    sex: Optional[str]
    age: Optional[float]
    sibsp: Optional[int]
    parch: Optional[int]
    ticket: Optional[str]
    fare: Optional[float]
    cabin: Optional[str]
    embarked: Optional[str]
    boat: Optional[str]      # mixed values like '2', 'D', '11'
    body: Optional[float]    # body ID numbers, NaN for survivors
    home_dest: Optional[str] # renamed from home.dest


class MultipleTitanicDataInputSchema(BaseModel):
    inputs: List[TitanicDataInputSchema]