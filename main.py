from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import os
import json
from typing import Optional

app = FastAPI()

# Allow your frontend origin (adjust as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST", "GET", "OPTIONS"],
    allow_headers=["*"],
)

# Car database with information and video paths
CAR_DATABASE = {
    "toyota_camry": {
        "make": "Toyota",
        "model": "Camry",
        "year": "2023",
        "purpose": "Family sedan designed for comfort and reliability. Perfect for daily commuting, family trips, and business travel. Known for its fuel efficiency and low maintenance costs.",
        "video_path": "videos/toyota_camry.mp4",
        "features": ["Hybrid option available", "Advanced safety features", "Spacious interior"]
    },
    "honda_civic": {
        "make": "Honda",
        "model": "Civic",
        "year": "2023",
        "purpose": "Compact car ideal for urban driving and young professionals. Offers sporty handling, excellent fuel economy, and modern technology features.",
        "video_path": "videos/honda_civic.mp4",
        "features": ["Sport mode", "Apple CarPlay/Android Auto", "Honda Sensing"]
    },
    "tesla_model3": {
        "make": "Tesla",
        "model": "Model 3",
        "year": "2023",
        "purpose": "Electric vehicle designed for performance and sustainability. Combines luxury features with zero emissions, perfect for environmentally conscious drivers.",
        "video_path": "videos/tesla_model3.mp4",
        "features": ["Autopilot", "Supercharging network", "Over-the-air updates"]
    }
}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # read the raw bytes (you'll run your model on these later)
    data = await file.read()
    
    # This is where you'd implement your actual car recognition model
    # For now, using dummy logic - replace with your ML model
    predicted_car = "toyota_camry"  # Replace with actual prediction
    
    # Get car information from database
    car_info = CAR_DATABASE.get(predicted_car, {
        "make": "unknown",
        "model": "unknown", 
        "year": "unknown",
        "purpose": "Car information not available in database",
        "video_path": None,
        "features": []
    })
    
    return {
        "filename": file.filename,
        "size_bytes": len(data),
        "prediction": {
            "make": car_info["make"],
            "model": car_info["model"],
            "year": car_info["year"],
            "confidence": 0.85,  # Replace with actual confidence 
            "purpose": car_info["purpose"],
            "features": car_info["features"],
            "video_available": car_info["video_path"] is not None
        }
    }

@app.get("/car/{car_id}/video")
async def get_car_video(car_id: str):
    """Get video for a specific car model"""
    if car_id not in CAR_DATABASE:
        raise HTTPException(status_code=404, detail="Car not found")
    
    video_path = CAR_DATABASE[car_id]["video_path"]
    if not video_path or not os.path.exists(video_path):
        raise HTTPException(status_code=404, detail="Video not found")
    
    return FileResponse(video_path, media_type="video/mp4")

@app.get("/cars")
async def get_all_cars():
    """Get information about all available cars"""
    return {
        "cars": [
            {
                "id": car_id,
                "make": info["make"],
                "model": info["model"],
                "year": info["year"],
                "purpose": info["purpose"],
                "features": info["features"]
            }
            for car_id, info in CAR_DATABASE.items()
        ]
    }

@app.get("/")
async def root():
    """API information and usage"""
    return {
        "message": "Car AI Recognition API",
        "endpoints": {
            "POST /predict": "Upload car image for recognition",
            "GET /car/{car_id}/video": "Get video for specific car model",
            "GET /cars": "Get all available car information"
        },
        "supported_formats": ["jpg", "jpeg", "png", "webp"]
    }
