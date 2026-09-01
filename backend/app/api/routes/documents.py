from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path
import uuid

router = APIRouter(prefix="/documents", tags=["Documents"])

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

ALLOWED_EXTENSIONS = {".pdf", ".png", ".jpg", ".jpeg"}

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    extension = Path(file.filename).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type. Use PDF, PNG, JPG, or JPEG."
        )

    document_id = str(uuid.uuid4())
    filename = f"{document_id}{extension}"
    file_path = UPLOAD_DIR / filename

    content = await file.read()
    file_path.write_bytes(content)

    return {
        "document_id": document_id,
        "filename": file.filename,
        "stored_filename": filename,
        "file_type": extension,
        "message": "Document uploaded successfully"
    }