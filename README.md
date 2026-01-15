# upperlimbfracturedetection
This project presents an AI-powered upper limb bone fracture detection system using the YOLOv8 object detection model. The system is designed to automatically identify and localize fractures in X-ray images of the upper limb, including the elbow, fingers, forearm, humerus, shoulder, and wrist.

📌 What I Did
Downloaded upper limb X-ray fracture dataset from Kaggle
Trained a YOLOv8 object detection model on GPU using Google Colab
Detected fractures in elbow, fingers, forearm, humerus, shoulder, and wrist
Deployed the trained model using FastAPI
Created a simple Streamlit web interface for predictions
Evaluated the trained model using standard detection metrics

To run the project:
cd upperlimbfracture
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --host 127.0.0.1 --port 8004 or (python -m uvicorn main:app --host 127.0.0.1 --port 8004)
split terminal 
streamlit run app.py or (python -m streamlit run app.py)

******************************
Documentation

**1. Problem Statement**

**Business / Real-World Problem**
Bone fracture diagnosis using X-ray images is a critical task in healthcare. Manual examination by radiologists can be time-consuming and may lead to missed fractures, especially when fractures are small or subtle. In emergency cases, quick and accurate detection is essential

**Objective**
To develop a YOLO-based deep learning model that automatically detects bone fractures in X-ray images by locating and identifying fracture regions in real time.
Success Criteria
-Correctly detect fracture regions in X-ray images
-Achieve high precision and recall
-Perform fast inference suitable for real-time medical assistance

**2. Dataset Description**

**Data Source:**
Publicly available Bone Fracture X-ray datasets from Kaggle.
Features
1.Input Feature:
-X-ray images
-Spatial features extracted automatically by YOLO

2.Target Variable
Bounding box coordinates of fractures
Class label: fracture

**3. Data Preprocessing & EDA**
**Data Cleaning**
-Removed duplicate and low-quality images
-Verified annotation accuracy

**Data Transformation**
-Resized images to YOLO-compatible input size (e.g., 640×640)
-Normalized pixel values
-Converted annotations to YOLO format

**EDA & Visualization**
-Visualized annotated bounding boxes on X-ray images
-Checked class distribution and annotation coverage

**Key Insights**
-Fractures vary significantly in size and location
-Some fractures are very subtle and difficult to detect
-Data augmentation improves robustness

**4. Modeling Approach**

**Model Choice Justification**
YOLO (You Only Look Once) was chosen because:

-It performs object detection and localization simultaneously
-Faster inference compared to traditional CNN classifiers
-Suitable for real-time applications
-High accuracy with end-to-end training

**Training Methodology**
-Used pre-trained YOLO weights (transfer learning)
-Fine-tuned model on fracture dataset
-Trained using batch-based gradient descent

**6. Evaluation**

**Evaluation Metrics**
-Precision
-Recall
-mAP (mean Average Precision)
-F1 Score

**Model Performance**
-Model achieved strong precision and recall for fracture detection
-Accurate localization of fracture regions
-Minor false negatives occurred in very faint fracture cases

**7. Conclusion & Future Scope**

**Final Insights**
-YOLO effectively detects bone fractures from X-ray images
-The system provides real-time fracture localization
-Can assist radiologists in emergency and clinical settings

**Limitations**
-Sensitive to low-contrast or noisy X-ray images
-Requires well-annotated bounding box data
-Limited dataset size affects generalization

**Future Improvements**
-Train on a larger multi-hospital dataset
-Use segmentation for more accuracy.
-Extend to multi-class detection (fracture types)
-Add explainable AI (heatmaps / Grad-CAM)
-Integrate into hospital web-based systems




