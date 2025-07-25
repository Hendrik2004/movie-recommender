from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np
import os

app = FastAPI()

# Middleware CORS para permitir peticiones desde el frontend HTML
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cargar modelos y número de features esperados
models = {
    "logistic_regression": {
        "model": joblib.load("models/logistic_regression.joblib"),
        "n_features": 20
    },
    "random_forest": {
        "model": joblib.load("models/random_forest.joblib"),
        "n_features": 20
    },
    "gradient_boosting": {
        "model": joblib.load("models/gradient_boosting.joblib"),
        "n_features": 20
    },
    "svm_rbf": {
        "model": joblib.load("models/svm_rbf.joblib"),
        "n_features": 20
    },
}

class ModelInput(BaseModel):
    features: list[float]
    model_name: str

@app.get("/", response_class=HTMLResponse)
def read_root():
    html_path = os.path.join(os.path.dirname(__file__), "app.html")
    if not os.path.exists(html_path):
        raise HTTPException(status_code=500, detail="Archivo app.html no encontrado.")
    with open(html_path, "r", encoding="utf-8") as f:
        return f.read()

@app.post("/predict/")
def predict(data: ModelInput):
    if data.model_name not in models:
        raise HTTPException(status_code=400, detail="Modelo no válido")

    model_info = models[data.model_name]
    model = model_info["model"]
    expected = model_info["n_features"]

    if len(data.features) != expected:
        raise HTTPException(
            status_code=400,
            detail=f"El modelo {data.model_name} espera {expected} features, pero se recibieron {len(data.features)}"
        )

    try:
        X = np.array(data.features).reshape(1, -1)
        prediction = model.predict(X)[0]
        return {"prediction": int(prediction)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error durante la predicción: {str(e)}")
