from fastapi import FastAPI, APIRouter, Depends, UploadFile
from fastapi.responses import JSONResponse
from helpers import getSetting, Settings
from services import DataService, ProcessService
import aiofiles
import logging
from .schemes import ProcessRequest
from models import ResponseMessage

logger = logging.getLogger('uvicorn.error')
data_router = APIRouter(
    prefix="/data",
    tags=["api_for_data"]  
)

@data_router.post("/upload/{project_id}")
async def upload(project_id: str, file: UploadFile, app_Settings: Settings = Depends(getSetting) ):

  
    file_path, final_filename = DataService().generate_unique_filepath(orig_file=file.filename, project_id= project_id)

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
            "full_path": str(file_path),
            "file id": final_filename
    
        }
    )

@data_router.post("/process/{project_id}")
async def process(project_id: str, request: ProcessRequest):
    
    final_filename = request.file_id
    chunk_size = request.chunk_size
    overlap_size = request.overlap_size

    process_service = ProcessService(project_id=project_id)
    file_content = process_service.get_file_content(final_filename=final_filename)
    chunks = process_service.split_content(content_file=file_content, final_name=final_filename, chunk_size=chunk_size, overlap_size=overlap_size)
    
    if chunks is None:
        return JSONResponse(
            status_code=400,
            content={
                "message":  ResponseMessage.PROCESSING_FAILED.value
            }
        )
    return chunks