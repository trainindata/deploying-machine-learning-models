from typing import List, Optional, Tuple

import numpy as np
import pandas as pd
from pydantic import BaseModel, ValidationError

from classification_model.config.core import config
from classification_model.processing.data_manager import preprocessing


def validate_inputs(*, input_data: pd.DataFrame) -> Tuple[pd.DataFrame, Optional[dict]]:
    """Check model inputs for unprocessable values."""

    # convert syntax error field names (beginning with numbers)
    input_data = preprocessing(data=input_data)
    validated_data = input_data[config.model_config.features].copy()
    errors = None

    try:
        # replace numpy nans so that pydantic can validate
        MultipleTitanicDataInputs(
            inputs=validated_data.replace({np.nan: None}).to_dict(orient="records")
        )
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
    boat: Optional[str]
    body: Optional[str]


class MultipleTitanicDataInputs(BaseModel):
    inputs: List[TitanicDataInputSchema]
