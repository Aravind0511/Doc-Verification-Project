from fastapi import FastAPI
from app.api.routes.documents import router as documents_router

app = FastAPI(
    title="Doc Verification API",
    description="OCR and Deep Learning-Based Document Verification With Blockchain-Enabled Tamper Detection",
    version="0.1.0"
)

app.include_router(documents_router)

@app.get("/")
def root():
    return {
        "message": "Doc Verification API is running"
    }