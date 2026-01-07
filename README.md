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


