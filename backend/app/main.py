from fastapi import FastAPI

app = FastAPI(
    title="Doc Verification API",
    description="OCR and Deep Learning-Based Document Verification With Blockchain-Enabled Tamper Detection",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "message": "Doc Verification API is running"
    }