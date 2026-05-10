# README.md
# Computer Vision Platform Backend

This repository contains a FastAPI backend for a computer vision platform. It supports image upload, simple inference using a pre‑trained model, and storage of images and labels in PostgreSQL.

## Setup

```bash
# Build image
docker build -t cv-backend .

# Run container
docker run -d -p 8000:8000 --env-file .env cv-backend
```

## Endpoints

- `POST /api/vision/upload` – Upload an image and get inference results.
- `GET /` – Health check.

## Dependencies
- FastAPI
- Uvicorn
- SQLAlchemy
- Torch / torchvision
- OpenCV
- Pillow

