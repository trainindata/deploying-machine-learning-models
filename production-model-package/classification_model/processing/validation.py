from typing import List, Optional, Tuple

import numpy as np
import pandas as pd
from pydantic import BaseModel, ValidationError

from classification_model.config.core import config

from .utils import get_first_cabin, get_title


def replace_na_inputs(*, input_data: pd.DataFrame) -> pd.DataFrame:
    """Replace na with ?"""
    valid_data = input_data.copy()
    valid_data.replace("?", np.nan, inplace=True)

    return valid_data


def get_first_cabin_inputs(*, input_data: pd.DataFrame) -> pd.DataFrame:
    """Get first cabin if more than 1"""
    valid_data = input_data.copy()
    valid_data[config.model_config.cabin[0]] = valid_data[
        config.model_config.cabin[0]
    ].apply(get_first_cabin)
    return valid_data


def get_title_inputs(*, input_data: pd.DataFrame) -> pd.DataFrame:
    """extracts the title (Mr, Ms, etc) from the name variable"""
    valid_data = input_data.copy()
    valid_data[config.model_config.title] = valid_data[config.model_config.name].apply(
        get_title
    )
    return valid_data


def get_elem_inputs(*, input_data: pd.DataFrame) -> pd.DataFrame:
    """Get element in cabin and title."""
    valid_data = input_data.copy()
    validated_data = get_first_cabin_inputs(input_data=valid_data)
    validated_data = get_title_inputs(input_data=validated_data)
    return validated_data


def validate_inputs(*, input_data: pd.DataFrame) -> Tuple[pd.DataFrame, Optional[dict]]:
    """Check model inputs for unprocessable values."""

    # convert syntax error field names (beginning with numbers)
    valid_data = input_data.copy()
    valid_data = valid_data.replace("?", np.nan)
    valid_data["Fare"] = valid_data["Fare"].astype("float")
    valid_data["Age"] = valid_data["Age"].astype("float")
    validated_data = get_elem_inputs(input_data=valid_data)
    validated_data = validated_data[
        config.model_config.features + [config.model_config.title]
    ].copy()
    # validated_data.drop(labels=config.model_config.variables_to_drop)
    errors = None
    try:
        # replace numpy nans so that pydantic can validate
        MultiplePassengerDataInputs(
            inputs=validated_data.replace({np.nan: None}).to_dict(orient="records")
        )
    except ValidationError as error:
        errors = error.json()

    return validated_data, errors


class TitanicDataInputSchema(BaseModel):
    PassengerId: Optional[int]
    Pclass: Optional[str]
    Name: Optional[str]
    Sex: Optional[str]
    Age: Optional[float]
    SibSp: Optional[str]
    Parch: Optional[str]
    Ticket: Optional[str]
    Fare: Optional[float]
    Cabin: Optional[str]
    Embarked: Optional[str]


class MultiplePassengerDataInputs(BaseModel):
    inputs: List[TitanicDataInputSchema]
