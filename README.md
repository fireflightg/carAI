
# CarVision 🚗📸  
AI-powered app that detects the type of car (make, model, year) from a photo.

## 🔍 What It Does
Upload or snap a photo of any car, and CarVision uses AI to:
- Detect the car in the image
- Predict the **make**, **model**, and **year**
- Show confidence scores and similar car images

## 🧠 Tech Stack

### 🖥️ Frontend
- **Next.js / React**
- **Tailwind CSS**
- Camera or file upload interface
- Displays results with cropped car preview and car info

### 🐍 Backend (Python)
- **YOLOv8** for object detection
- **Pretrained classifier** on car make/model/year
- **FastAPI** to handle image uploads and return predictions
- Optional: **EasyOCR** for license plate detection

## 📦 Features
- Upload or take photo of a car
- Instant predictions from AI model
- Car image crop with bounding box
- Option to save to history (coming soon)
- Fun facts and links about the predicted car

## 🛠 How to Run

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
````

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## 📁 Folder Structure

```
carvision/
│
├── frontend/          # React or Next.js app
│   ├── components/
│   ├── pages/
│   └── ...
│
├── backend/           # FastAPI + model files
│   ├── main.py
│   ├── models/
│   └── ...
```

## ⚡ Future Features

* OCR license plate detection
* Reverse image search for similar cars
* Map of most common cars by type

```
