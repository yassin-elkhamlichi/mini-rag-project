from fastapi import FastAPI, APIRouter, Depends, UploadFile
from fastapi.responses import JSONResponse
from helpers import getSetting, Settings
from services import DataController


data_router = APIRouter(
    prefix="/data",
    tags=["api_for_data"]  
)

@data_router.post("/upload/{project_id}")
async def upload(project_id: str, file: UploadFile, app_Settings: Settings = Depends(getSetting) ):

    is_valid, result_signal = DataController().validate_upload_file(file=file)

    return JSONResponse(
        status_code=201,
        content={
            "message": "File uploaded successfully",
            "file_name": file.filename
        }
    )