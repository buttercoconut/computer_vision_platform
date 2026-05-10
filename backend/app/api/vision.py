# app/api/vision.py
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from fastapi.responses import JSONResponse
import io
import cv2
import numpy as np
import torch
from torchvision import transforms
from PIL import Image
from app.database.database import get_db
from app.models.image import Image as ImageModel
from app.models.label import Label
from sqlalchemy.orm import Session

router = APIRouter()

# Simple model loader (placeholder)
MODEL_PATH = "/models/resnet18.pt"
try:
    model = torch.load(MODEL_PATH, map_location="cpu")
    model.eval()
except Exception:
    model = None

# Preprocess transform
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

@router.post("/upload")
async def upload_image(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Unsupported file type")
    contents = await file.read()
    # Store image in DB
    image_obj = ImageModel(filename=file.filename, content_type=file.content_type, data=contents)
    db.add(image_obj)
    db.commit()
    db.refresh(image_obj)

    # Run inference
    if model is None:
        return JSONResponse(status_code=503, content={"detail": "Model not loaded"})

    # Convert bytes to PIL
    pil_img = Image.open(io.BytesIO(contents)).convert("RGB")
    input_tensor = transform(pil_img).unsqueeze(0)
    with torch.no_grad():
        outputs = model(input_tensor)
    # Dummy label extraction (using ImageNet classes placeholder)
    _, preds = torch.max(outputs, 1)
    label_name = f"class_{preds.item()}"
    confidence = float(outputs[0, preds].item())

    # Store label
    label_obj = Label(image_id=image_obj.id, category=label_name, confidence=str(confidence))
    db.add(label_obj)
    db.commit()

    return {"image_id": image_obj.id, "label": label_name, "confidence": confidence}
