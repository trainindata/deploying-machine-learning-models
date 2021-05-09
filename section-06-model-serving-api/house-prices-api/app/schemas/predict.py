from pydantic import BaseModel
from typing import Optional, Any, List


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    predictions: Optional[List[float]]
