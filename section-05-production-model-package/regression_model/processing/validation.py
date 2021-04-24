from typing import Tuple, Optional, List
from regression_model.config.core import config

from pydantic import BaseModel, ValidationError
import numpy as np
import pandas as pd


def drop_na_inputs(*, input_data: pd.DataFrame) -> pd.DataFrame:
    """Check model inputs for na values and filter."""
    validated_data = input_data.copy()
    new_vars_with_na = [
        var for var in config.model_config.features
        if var not in config.model_config.categorical_vars_with_na_frequent +
           config.model_config.categorical_vars_with_na_missing +
           config.model_config.numerical_vars_with_na
           and validated_data[var].isnull().sum() > 0
    ]
    validated_data.dropna(subset=new_vars_with_na, inplace=True)

    return validated_data


def validate_inputs(
        *, input_data: pd.DataFrame
) -> Tuple[pd.DataFrame, Optional[dict]]:
    """Check model inputs for unprocessable values."""

    # convert syntax error field names (beginning with numbers)
    input_data.rename(columns=config.model_config.variables_to_rename, inplace=True)
    input_data.drop('Id', axis=1, inplace=True)
    input_data['MSSubClass'] = input_data['MSSubClass'].astype('O')
    validated_data = drop_na_inputs(input_data=input_data)
    errors = None

    try:
        # replace numpy nans so that pydantic can validate
        MultipleHouseDataInputs(inputs=validated_data.replace({np.nan: None}).to_dict(orient="records"))
    except ValidationError as error:
        errors = error.json()

    return validated_data, errors


class HouseDataInputSchema(BaseModel):
    Alley: Optional[str]
    BedroomAbvGr: int
    BldgType: str
    BsmtCond: Optional[str]
    BsmtExposure: Optional[str]
    BsmtFinSF1: Optional[float]
    BsmtFinSF2: Optional[float]
    BsmtFinType1: Optional[str]
    BsmtFinType2: Optional[str]
    BsmtFullBath: Optional[float]
    BsmtHalfBath: Optional[float]
    BsmtQual: Optional[str]
    BsmtUnfSF: float
    CentralAir: str
    Condition1: str
    Condition2: str
    Electrical: Optional[str]
    EnclosedPorch: int
    ExterCond: str
    ExterQual: str
    Exterior1st: Optional[str]
    Exterior2nd: Optional[str]
    Fence: Optional[str]
    FireplaceQu: Optional[str]
    Fireplaces: int
    Foundation: str
    FullBath: int
    Functional: Optional[str]
    GarageArea : float
    GarageCars : float
    GarageCond: Optional[str]
    GarageFinish: Optional[str]
    GarageQual: Optional[str]
    GarageType: Optional[str]
    GarageYrBlt: Optional[float]
    GrLivArea: int
    HalfBath: int
    Heating: str
    HeatingQC: str
    HouseStyle: str
    Id: Optional[int]
    KitchenAbvGr: int
    KitchenQual: Optional[str]
    LandContour: str
    LandSlope: str
    LotArea: int
    LotConfig: str
    LotFrontage: Optional[float]
    LotShape: str
    LowQualFinSF: int
    MSSubClass: int
    MSZoning: Optional[str]
    MasVnrArea: Optional[float]
    MasVnrType: Optional[str]
    MiscFeature: Optional[str]
    MiscVal: int
    MoSold: int
    Neighborhood: str
    OpenPorchSF: int
    OverallCond: int
    OverallQual: int
    PavedDrive: str
    PoolArea: int
    PoolQC: Optional[str]
    RoofMatl: str
    RoofStyle: str
    SaleCondition: str
    SaleType: Optional[str]
    ScreenPorch: int
    Street: str
    TotRmsAbvGrd: int
    TotalBsmtSF : float
    Utilities: Optional[str]
    WoodDeckSF: int
    YearBuilt: int
    YearRemodAdd: int
    YrSold: int
    FirstFlrSF: int  # renamed
    SecondFlrSF: int  # renamed
    ThreeSsnPortch: int  # renamed


class MultipleHouseDataInputs(BaseModel):
    inputs: List[HouseDataInputSchema]