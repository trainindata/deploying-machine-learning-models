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
        if var
        not in config.model_config.categorical_vars_with_na_frequent
        + config.model_config.categorical_vars_with_na_missing
        + config.model_config.numerical_vars_with_na
        and validated_data[var].isnull().sum() > 0
    ]
    validated_data.dropna(subset=new_vars_with_na, inplace=True)

    return validated_data


def validate_inputs(*, input_data: pd.DataFrame) -> Tuple[pd.DataFrame, Optional[dict]]:
    """Check model inputs for unprocessable values."""

    # convert syntax error field names (beginning with numbers)
    input_data.rename(columns=config.model_config.variables_to_rename, inplace=True)
    input_data["MSSubClass"] = input_data["MSSubClass"].astype("O")
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


class HouseDataInputSchema(BaseModel):
    Alley: Optional[str]
    BedroomAbvGr: Optional[int]
    BldgType: Optional[str]
    BsmtCond: Optional[str]
    BsmtExposure: Optional[str]
    BsmtFinSF1: Optional[float]
    BsmtFinSF2: Optional[float]
    BsmtFinType1: Optional[str]
    BsmtFinType2: Optional[str]
    BsmtFullBath: Optional[float]
    BsmtHalfBath: Optional[float]
    BsmtQual: Optional[str]
    BsmtUnfSF: Optional[float]
    CentralAir: Optional[str]
    Condition1: Optional[str]
    Condition2: Optional[str]
    Electrical: Optional[str]
    EnclosedPorch: Optional[int]
    ExterCond: Optional[str]
    ExterQual: Optional[str]
    Exterior1st: Optional[str]
    Exterior2nd: Optional[str]
    Fence: Optional[str]
    FireplaceQu: Optional[str]
    Fireplaces: Optional[int]
    Foundation: Optional[str]
    FullBath: Optional[int]
    Functional: Optional[str]
    GarageArea: Optional[float]
    GarageCars: Optional[float]
    GarageCond: Optional[str]
    GarageFinish: Optional[str]
    GarageQual: Optional[str]
    GarageType: Optional[str]
    GarageYrBlt: Optional[float]
    GrLivArea: Optional[int]
    HalfBath: Optional[int]
    Heating: Optional[str]
    HeatingQC: Optional[str]
    HouseStyle: Optional[str]
    Id: Optional[int]
    KitchenAbvGr: Optional[int]
    KitchenQual: Optional[str]
    LandContour: Optional[str]
    LandSlope: Optional[str]
    LotArea: Optional[int]
    LotConfig: Optional[str]
    LotFrontage: Optional[float]
    LotShape: Optional[str]
    LowQualFinSF: Optional[int]
    MSSubClass: Optional[int]
    MSZoning: Optional[str]
    MasVnrArea: Optional[float]
    MasVnrType: Optional[str]
    MiscFeature: Optional[str]
    MiscVal: Optional[int]
    MoSold: Optional[int]
    Neighborhood: Optional[str]
    OpenPorchSF: Optional[int]
    OverallCond: Optional[int]
    OverallQual: Optional[int]
    PavedDrive: Optional[str]
    PoolArea: Optional[int]
    PoolQC: Optional[str]
    RoofMatl: Optional[str]
    RoofStyle: Optional[str]
    SaleCondition: Optional[str]
    SaleType: Optional[str]
    ScreenPorch: Optional[int]
    Street: Optional[str]
    TotRmsAbvGrd: Optional[int]
    TotalBsmtSF: Optional[float]
    Utilities: Optional[str]
    WoodDeckSF: Optional[int]
    YearBuilt: Optional[int]
    YearRemodAdd: Optional[int]
    YrSold: Optional[int]
    FirstFlrSF: Optional[int]  # renamed
    SecondFlrSF: Optional[int]  # renamed
    ThreeSsnPortch: Optional[int]  # renamed


class MultipleHouseDataInputs(BaseModel):
    inputs: List[HouseDataInputSchema]
