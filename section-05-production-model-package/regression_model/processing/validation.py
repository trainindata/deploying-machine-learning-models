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
        for var in config.model_settings.features
        if var
        not in config.model_settings.categorical_vars_with_na_frequent
        + config.model_settings.categorical_vars_with_na_missing
        + config.model_settings.numerical_vars_with_na
        and validated_data[var].isnull().sum() > 0
    ]
    validated_data.dropna(subset=new_vars_with_na, inplace=True)

    return validated_data


def validate_inputs(*, input_data: pd.DataFrame) -> Tuple[pd.DataFrame, Optional[dict]]:
    """Check model inputs for unprocessable values."""

    # convert syntax error field names (beginning with numbers)
    input_data.rename(columns=config.model_settings.variables_to_rename, inplace=True)
    input_data["MSSubClass"] = input_data["MSSubClass"].astype("O")
    relevant_data = input_data[config.model_settings.features].copy()

    # Keep categorical features as object for feature-engine checks.
    for var in config.model_settings.categorical_vars:
        relevant_data[var] = relevant_data[var].astype("O")

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
    Alley: Optional[str] = None
    BedroomAbvGr: Optional[int] = None
    BldgType: Optional[str] = None
    BsmtCond: Optional[str] = None
    BsmtExposure: Optional[str] = None
    BsmtFinSF1: Optional[float] = None
    BsmtFinSF2: Optional[float] = None
    BsmtFinType1: Optional[str] = None
    BsmtFinType2: Optional[str] = None
    BsmtFullBath: Optional[float] = None
    BsmtHalfBath: Optional[float] = None
    BsmtQual: Optional[str] = None
    BsmtUnfSF: Optional[float] = None
    CentralAir: Optional[str] = None
    Condition1: Optional[str] = None
    Condition2: Optional[str] = None
    Electrical: Optional[str] = None
    EnclosedPorch: Optional[int] = None
    ExterCond: Optional[str] = None
    ExterQual: Optional[str] = None
    Exterior1st: Optional[str] = None
    Exterior2nd: Optional[str] = None
    Fence: Optional[str] = None
    FireplaceQu: Optional[str] = None
    Fireplaces: Optional[int] = None
    Foundation: Optional[str] = None
    FullBath: Optional[int] = None
    Functional: Optional[str] = None
    GarageArea: Optional[float] = None
    GarageCars: Optional[float] = None
    GarageCond: Optional[str] = None
    GarageFinish: Optional[str] = None
    GarageQual: Optional[str] = None
    GarageType: Optional[str] = None
    GarageYrBlt: Optional[float] = None
    GrLivArea: Optional[int] = None
    HalfBath: Optional[int] = None
    Heating: Optional[str] = None
    HeatingQC: Optional[str] = None
    HouseStyle: Optional[str] = None
    Id: Optional[int] = None
    KitchenAbvGr: Optional[int] = None
    KitchenQual: Optional[str] = None
    LandContour: Optional[str] = None
    LandSlope: Optional[str] = None
    LotArea: Optional[int] = None
    LotConfig: Optional[str] = None
    LotFrontage: Optional[float] = None
    LotShape: Optional[str] = None
    LowQualFinSF: Optional[int] = None
    MSSubClass: Optional[int] = None
    MSZoning: Optional[str] = None
    MasVnrArea: Optional[float] = None
    MasVnrType: Optional[str] = None
    MiscFeature: Optional[str] = None
    MiscVal: Optional[int] = None
    MoSold: Optional[int] = None
    Neighborhood: Optional[str] = None
    OpenPorchSF: Optional[int] = None
    OverallCond: Optional[int] = None
    OverallQual: Optional[int] = None
    PavedDrive: Optional[str] = None
    PoolArea: Optional[int] = None
    PoolQC: Optional[str] = None
    RoofMatl: Optional[str] = None
    RoofStyle: Optional[str] = None
    SaleCondition: Optional[str] = None
    SaleType: Optional[str] = None
    ScreenPorch: Optional[int] = None
    Street: Optional[str] = None
    TotRmsAbvGrd: Optional[int] = None
    TotalBsmtSF: Optional[float] = None
    Utilities: Optional[str] = None
    WoodDeckSF: Optional[int] = None
    YearBuilt: Optional[int] = None
    YearRemodAdd: Optional[int] = None
    YrSold: Optional[int] = None
    FirstFlrSF: Optional[int] = None  # renamed
    SecondFlrSF: Optional[int] = None  # renamed
    ThreeSsnPortch: Optional[int] = None  # renamed


class MultipleHouseDataInputs(BaseModel):
    inputs: List[HouseDataInputSchema]
