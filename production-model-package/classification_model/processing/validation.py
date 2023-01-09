from typing import List, Optional, Tuple
from utils import get_first_cabin, get_title

import numpy as np
import pandas as pd
from pydantic import BaseModel, ValidationError

from classification_model.config.core import config


def replace_na_inputs(*, input_data: pd.DataFrame) -> pd.DataFrame:
    """Replace na with ?"""
    valid_data = input_data.copy()
    valid_data.replace('?', np.nan, inplace=True)

    return valid_data


def get_first_cabin_inputs(*, input_data: pd.DataFrame) -> pd.DataFrame:
    """Get first cabin if more than 1"""
    valid_data = input_data.copy()
    valid_data[config.model_config.cabin[0]] = valid_data[config.model_config.cabin[0]].apply(get_first_cabin)
    return valid_data


def get_title_inputs(*, input_data: pd.DataFrame) -> pd.DataFrame:
    """extracts the title (Mr, Ms, etc) from the name variable"""
    valid_data = input_data.copy()
    valid_data[config.model_config.title] = valid_data[config.model_config.name].apply(get_title)

    return valid_data


def drop_na_inputs(*, input_data: pd.DataFrame) -> pd.DataFrame:
    """Check model inputs for na values and filter."""
    validated_data = input_data.copy()
    new_vars_with_na = config.model_config.features
    validated_data.dropna(subset=new_vars_with_na, inplace=True)

    return validated_data


def validate_inputs(*, input_data: pd.DataFrame) -> Tuple[pd.DataFrame, Optional[dict]]:
    """Check model inputs for unprocessable values."""

    # convert syntax error field names (beginning with numbers)
    input_data.drop(labels=config.model_config.variables_to_drop, axis=1, inplace=True, inplace=True)
    input_data['Fare'] = input_data['Fare'].astype('float')
    input_data['Age'] = input_data['Age'].astype('float')
    relevant_data = input_data[config.model_config.features].copy()
    validated_data = drop_na_inputs(input_data=relevant_data)
    errors = None

    try:
        # replace numpy nans so that pydantic can validate
        MultipleHouseDataInputs(
            inputs=validated_data.replace({np.nan: None}).to_dict(orient="records")
        )
    except ValidationError as error:
        errors = error.json()

    return validated_data, errors



class TitanicDataInputSchema(BaseModel):
    Pclass: Optional[str]
    Name: Optional[str]
    Sex: Optional[str]
    Age: Optional[int]
    SibSp: Optional[str]
    Parch: Optional[float]
    Ticket: Optional[float]
    Fare: Optional[int]
    Cabin: Optional[str]
    Embarked: Optional[float]



class MultipleHouseDataInputs(BaseModel):
    inputs: List[TitanicDataInputSchema]
