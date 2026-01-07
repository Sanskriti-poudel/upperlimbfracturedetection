FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip

#PyTorch CPU install
RUN pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8003 8501

# 🔹 Start FastAPI + Streamlit
CMD ["bash", "-c", "uvicorn backend.main:app --host 0.0.0.0 --port 8003 & streamlit run frontend/app.py --server.port 8501 --server.address 0.0.0.0"]
