# import typing as t
#
# from regression_model.config.core import config
#
# import numpy as np
# import pandas as pd
#
#
# # TODO: replace with pydantic
# class HouseDataInputSchema(Schema):
#     Alley = fields.Str(allow_none=True)
#     BedroomAbvGr = fields.Integer()
#     BldgType = fields.Str()
#     BsmtCond = fields.Str(allow_none=True)
#     BsmtExposure = fields.Str(allow_none=True)
#     BsmtFinSF1 = fields.Float(allow_none=True)
#     BsmtFinSF2 = fields.Float(allow_none=True)
#     BsmtFinType1 = fields.Str(allow_none=True)
#     BsmtFinType2 = fields.Str(allow_none=True)
#     BsmtFullBath = fields.Float(allow_none=True)
#     BsmtHalfBath = fields.Float(allow_none=True)
#     BsmtQual = fields.Str(allow_none=True)
#     BsmtUnfSF = fields.Float()
#     CentralAir = fields.Str()
#     Condition1 = fields.Str()
#     Condition2 = fields.Str()
#     Electrical = fields.Str(allow_none=True)
#     EnclosedPorch = fields.Integer()
#     ExterCond = fields.Str()
#     ExterQual = fields.Str()
#     Exterior1st = fields.Str(allow_none=True)
#     Exterior2nd = fields.Str(allow_none=True)
#     Fence = fields.Str(allow_none=True)
#     FireplaceQu = fields.Str(allow_none=True)
#     Fireplaces = fields.Integer()
#     Foundation = fields.Str()
#     FullBath = fields.Integer()
#     Functional = fields.Str(allow_none=True)
#     GarageArea = fields.Float()
#     GarageCars = fields.Float()
#     GarageCond = fields.Str(allow_none=True)
#     GarageFinish = fields.Str(allow_none=True)
#     GarageQual = fields.Str(allow_none=True)
#     GarageType = fields.Str(allow_none=True)
#     GarageYrBlt = fields.Float(allow_none=True)
#     GrLivArea = fields.Integer()
#     HalfBath = fields.Integer()
#     Heating = fields.Str()
#     HeatingQC = fields.Str()
#     HouseStyle = fields.Str()
#     Id = fields.Integer()
#     KitchenAbvGr = fields.Integer()
#     KitchenQual = fields.Str(allow_none=True)
#     LandContour = fields.Str()
#     LandSlope = fields.Str()
#     LotArea = fields.Integer()
#     LotConfig = fields.Str()
#     LotFrontage = fields.Float(allow_none=True)
#     LotShape = fields.Str()
#     LowQualFinSF = fields.Integer()
#     MSSubClass = fields.Integer()
#     MSZoning = fields.Str(allow_none=True)
#     MasVnrArea = fields.Float(allow_none=True)
#     MasVnrType = fields.Str(allow_none=True)
#     MiscFeature = fields.Str(allow_none=True)
#     MiscVal = fields.Integer()
#     MoSold = fields.Integer()
#     Neighborhood = fields.Str()
#     OpenPorchSF = fields.Integer()
#     OverallCond = fields.Integer()
#     OverallQual = fields.Integer()
#     PavedDrive = fields.Str()
#     PoolArea = fields.Integer()
#     PoolQC = fields.Str(allow_none=True)
#     RoofMatl = fields.Str()
#     RoofStyle = fields.Str()
#     SaleCondition = fields.Str()
#     SaleType = fields.Str(allow_none=True)
#     ScreenPorch = fields.Integer()
#     Street = fields.Str()
#     TotRmsAbvGrd = fields.Integer()
#     TotalBsmtSF = fields.Float()
#     Utilities = fields.Str(allow_none=True)
#     WoodDeckSF = fields.Integer()
#     YearBuilt = fields.Integer()
#     YearRemodAdd = fields.Integer()
#     YrSold = fields.Integer()
#     FirstFlrSF = fields.Integer()
#     SecondFlrSF = fields.Integer()
#     ThreeSsnPortch = fields.Integer()
#
#
# def drop_na_inputs(*, input_data: pd.DataFrame) -> pd.DataFrame:
#     """Check model inputs for na values and filter."""
#     validated_data = input_data.copy()
#     if input_data[config.model_config.numerical_na_not_allowed].isnull().any().any():
#         validated_data = validated_data.dropna(
#             axis=0, subset=config.model_config.numerical_na_not_allowed
#         )
#
#     return validated_data
#
#
# def validate_inputs(
#         *, input_data: pd.DataFrame
# ) -> t.Tuple[pd.DataFrame, t.Optional[dict]]:
#     """Check model inputs for unprocessable values."""
#
#     # convert syntax error field names (beginning with numbers)
#     input_data.rename(columns=config.model_config.variables_to_rename, inplace=True)
#     validated_data = drop_na_inputs(input_data=input_data)
#
#     # set many=True to allow passing in a list
#     schema = HouseDataInputSchema(many=True)
#     errors = None
#
#     try:
#         # replace numpy nans so that Marshmallow can validate
#         schema.load(validated_data.replace({np.nan: None}).to_dict(orient="records"))
#     except ValidationError as exc:
#         errors = exc.messages
#
#     return validated_data, errors
