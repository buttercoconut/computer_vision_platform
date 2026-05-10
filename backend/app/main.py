# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import vision

app = FastAPI(title="Computer Vision Platform API")

# CORS settings for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vue dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(vision.router, prefix="/api/vision", tags=["vision"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Computer Vision Platform API"}
