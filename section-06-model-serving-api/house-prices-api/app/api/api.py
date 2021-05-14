import json
import numpy as np
import pandas as pd
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from regression_model import __version__ as model_version
from regression_model.predict import make_prediction
from typing import Any

from app import __version__
from app import schemas
from app.config import settings

api_router = APIRouter()


@api_router.get("/", response_model=schemas.Msg, status_code=200)
def root() -> dict:
    """
    Root Get
    """
    return {"msg": "This is the Example API"}


@api_router.get("/health", response_model=schemas.Health, status_code=200)
def health() -> dict:
    """
    Root Get
    """
    health = schemas.Health(
        name=settings.PROJECT_NAME,
        api_version=__version__,
        model_version=model_version
    )

    return health.dict()


@api_router.post("/predict", response_model=schemas.PredictionResults, status_code=200)
async def predict(input_data: schemas.MultipleHouseDataInputs) -> Any:
    """
    Make house price predictions with the TID regression model
    """

    input_df = pd.DataFrame(jsonable_encoder(input_data.inputs))
    results = make_prediction(input_data=input_df.replace({np.nan: None}))
    if results['errors'] is not None:
        raise HTTPException(
            status_code=400,
            detail=json.loads(results['errors'])
        )

    return results