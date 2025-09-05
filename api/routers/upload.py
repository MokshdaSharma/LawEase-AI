from fastapi import APIRouter, UploadFile, File
import os
from api.config import settings

router = APIRouter()
os.makedirs(settings.STORAGE_PATH, exist_ok=True)

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(settings.STORAGE_PATH, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())
    return {"filename": file.filename, "path": file_path}
