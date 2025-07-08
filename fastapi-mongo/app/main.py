from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from app.database import get_patient_collection  # ✅ Assumes app/database.py is present
from bson import ObjectId
from fastapi.encoders import jsonable_encoder
from typing import List

from app.models import PatientCreate, PatientResponse
from app.database import get_patient_collection

app = FastAPI(title="Hospital Patient API")

# ✅ Pydantic model for request validation and response
# for testing purposes
# testing other thing
class Patient(BaseModel):
    name: str
    age: int
    gender: str
    condition: str

@app.get("/")
def home():
    return {"message": "Welcome to the Hospital API"}

@app.post("/patients", response_model=PatientResponse)
def create_patient(patient: PatientCreate):
    collection = get_patient_collection()
    patient_dict = jsonable_encoder(patient)
    result = collection.insert_one(patient_dict)
    created_patient = collection.find_one({"_id": result.inserted_id})
    return created_patient  # Will be serialized properly using PatientResponse

@app.get("/patients", response_model=List[PatientResponse])
def get_patients():
    collection = get_patient_collection()
    patients = list(collection.find())
    return patients
