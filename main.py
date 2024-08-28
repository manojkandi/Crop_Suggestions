from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import uvicorn 

# Load the trained model
model = joblib.load("random_forest_model.pkl")

app = FastAPI()

class SoilData(BaseModel):
    N: float
    P: float
    K: float
    ph: float

@app.get("/")
async def read_root():
    print("getting record")
    return {"crop selection web page"}

@app.post("/predict/")
async def predict_crop(data: SoilData): 
    try:
        features = np.array([[data.N, data.P, data.K, data.ph]])
        prediction = model.predict(features)
        return {"crop": prediction[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
