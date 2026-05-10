# api/vision.py
from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import base64
import os
import uuid
from pathlib import Path

from app.services.inference_service import run_inference
from app.schemas import InferenceResponse

router = APIRouter()

UPLOAD_DIR = Path("/tmp/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@router.post("/infer", response_model=InferenceResponse)
async def infer_image(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        # Save to temp file
        temp_path = UPLOAD_DIR / f"{uuid.uuid4()}_{file.filename}"
        with open(temp_path, "wb") as f:
            f.write(contents)
        # Run inference
        results = await run_inference(str(temp_path))
        # Clean up
        temp_path.unlink(missing_ok=True)
        return InferenceResponse(results=results)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Optional: health check
@router.get("/health")
async def health():
    return JSONResponse({"status": "ok"})
