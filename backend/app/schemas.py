# schemas.py
from pydantic import BaseModel
from typing import List, Optional

class ImageUploadRequest(BaseModel):
    filename: str
    content: str  # base64 encoded string

class InferenceResult(BaseModel):
    label: str
    confidence: float

class InferenceResponse(BaseModel):
    results: List[InferenceResult]
