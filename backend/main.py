from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from ultralytics import YOLO
from PIL import Image
import io
import numpy as np
import os

app = FastAPI(title="Bone Fracture Detection API")

# Allow Streamlit access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- LOAD YOLO MODEL ---------------- #

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

YOLO_MODEL_PATH = os.path.join(
    BASE_DIR,
    "..",
    "boneimages",
    "yolo_runs",
    "run1",
    "weights",
    "best.pt"
)

model = YOLO(YOLO_MODEL_PATH)

CLASS_NAMES = [
    "elbow positive",
    "fingers positive",
    "forearm fracture",
    "humerus fracture",
    "humerus",
    "shoulder fracture",
    "wrist positive"
]

# ---------------- ROUTES ---------------- #

@app.get("/")
def home():
    return {"message": "YOLO Bone Fracture Detection API running"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    try:
        results = model(image, conf=0.1)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Error during model prediction"
    )



    detections = []

    for r in results:
        if r.boxes is None:
            continue

        for box in r.boxes:
            cls_id = int(box.cls)
            conf = float(box.conf)
            x1, y1, x2, y2 = map(float, box.xyxy[0])

            detections.append({
                "class": CLASS_NAMES[cls_id],
                "confidence": round(conf, 4),
                "bbox": [x1, y1, x2, y2]
            })

    return {
        "total_detections": len(detections),
        "detections": detections
    }
