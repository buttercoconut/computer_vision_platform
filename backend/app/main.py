from fastapi import FastAPI
from app.api import vision

app = FastAPI(title="Computer Vision Platform API")

# Include routers
app.include_router(vision.router, prefix="/api/vision", tags=["vision"])

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the Computer Vision Platform API"}
