from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "TrialMatch AI API running"}