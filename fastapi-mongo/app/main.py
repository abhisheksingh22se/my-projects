from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from app.database import get_patient_collection  # ✅ Assumes app/database.py is present
from bson import ObjectId
from fastapi.encoders import jsonable_encoder

app = FastAPI(title="Hospital Patient API")

# ✅ Pydantic model for request validation and response
# for testing purposes
class Patient(BaseModel):
    name: str
    age: int
    gender: str
    condition: str

@app.get("/")
def home():
    return {"message": "Welcome to the Hospital API"}

@app.post("/patients")
def create_patient(patient: Patient):
    collection = get_patient_collection()
    patient_dict = jsonable_encoder(patient)  # 🔍 Safe conversion to avoid serialization issues
    result = collection.insert_one(patient_dict)
    return {"id": str(result.inserted_id), "message": "Patient added successfully"}

@app.get("/patients", response_model=List[Patient])
def get_patients():
    collection = get_patient_collection()
    patients_cursor = collection.find({}, {"_id": 0})  # 👈 Assumes no _id is needed
    patients = list(patients_cursor)
    return patients
