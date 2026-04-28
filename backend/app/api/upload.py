import os
import shutil
from fastapi import APIRouter, UploadFile, File

from app.agents.graph import build_graph
from app.api.chat import memory_store

router = APIRouter(prefix="/upload", tags=["Upload"])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

graph = build_graph()


@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = graph.invoke({
        "file_path": file_path
    })

    session_id = file.filename

    memory_store[session_id] = {
        "patient_profile": result.get("patient_profile"),
        "ranked_trials": result.get("ranked_trials"),
        "explanation": result.get("explanation"),
    }

    return {
        "session_id": session_id,
        "patient_profile": result.get("patient_profile"),
        "ranked_trials": result.get("ranked_trials"),
        "explanation": result.get("explanation"),
    }