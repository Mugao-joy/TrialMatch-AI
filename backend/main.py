from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.upload import router as upload_router
from app.db.database import engine
from app.db.models import Base
from app.api.chat import router as chat_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="TrialMatch AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router)
app.include_router(chat_router)


@app.get("/")
def root():
    return {"message": "TrialMatch AI API running"}