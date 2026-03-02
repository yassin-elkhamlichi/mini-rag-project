from fastapi import FastAPI, APIRouter, Depends, UploadFile
from fastapi.responses import JSONResponse
from helpers import getSetting, Settings
from controllers import DataController, ProjectController
import aiofiles
import logging

logger = logging.getLogger('uvicorn.error')
data_router = APIRouter(
    prefix="/data",
    tags=["api_for_data"]  
)

@data_router.post("/upload/{project_id}")
async def upload(project_id: str, file: UploadFile, app_Settings: Settings = Depends(getSetting) ):

    is_valid, result_signal = DataController().validate_upload_file(file=file)

   
    file_path = DataController().generate_unique_filename(orig_file=file.filename, project_id= project_id)

    try:
        async with aiofiles.open(file_path, "wb") as f:
            while chunk := await file.read(app_Settings.FILE_DEFAULT_CHUNK):
                await f.write(chunk)
    except Exception as e:

        logger.error(f"error while uploading file: {e}")
        
        return JSONResponse(
            status_code = 400,
            content={
                "message": "File filed to uploaded"
            }
        )


    return JSONResponse(
        content={
            "message": "File uploaded successfully",
            "file_name": file.filename,
            "full_path": str(file_path)
        }
    )