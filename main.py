from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

from functions.predict import predict
from functions.train import train

app = FastAPI()

class Body(BaseModel):
    texts: List[str]

@app.post("/train")
def update_neural_network():
    dataset = "helpers/dataset.csv"
    train(dataset)
    return {"message": "dataset is trained"}

@app.post("/predict")
def read_item(body: Body):
    predictions = predict(body.texts)
    return {"predictions": predictions}

# Pour exécuter: uvicorn main:app --reload
