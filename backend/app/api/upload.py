import os
import shutil
from fastapi import APIRouter, UploadFile, File

from app.services.extract_text import extract_text
from app.services.llm_extractor import extract_patient_profile
from app.services.trial_search import search_trials

router = APIRouter(prefix="/upload", tags=["Upload"])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    extracted_text = extract_text(file_path)

    patient_profile = extract_patient_profile(extracted_text)

    diagnosis = patient_profile.get("diagnosis", "")

    trials = search_trials(diagnosis)

    return {
        "patient_profile": patient_profile,
        "trials": trials,
    }