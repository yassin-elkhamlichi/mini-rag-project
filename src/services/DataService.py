from fastapi import UploadFile, status, HTTPException
from .BaseService import BaseService
from models import ResponseMessage
from .ProjectService import ProjectService
import re

class DataService(BaseService):
    
    def __init__(self):
        super().__init__()
        self.convert = 1024 * 1024
    
    def validate_upload_file(self, file: UploadFile):


        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            raise HTTPException(
                status_code = status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
                detail = ResponseMessage.UNSUPPORTED_MEDIA_TYPE.value
            )
        
        if file.size > self.app_settings.FILE_MAX_SIZE * self.convert:
           raise HTTPException(
                status_code = status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
                detail = ResponseMessage.REQUEST_ENTITY_TOO_LARGE.value
            )
        
        return True , "success"

    def generate_unique_filepath(self, orig_file: str, project_id: str):

       project_path = ProjectService().get_project_path(project_id=project_id)
       cleaned_name_file = self.clean_filename(orig_file=orig_file)

       while True:
       
            random_string = self.generate_random_string()
            final_filename = f"{random_string}_{cleaned_name_file}"
            new_file_path = project_path / final_filename

        
            if not new_file_path.exists():
                break
            
        
       return new_file_path, final_filename

    def clean_filename(self, orig_file: str):
        
        cleaned_file_name = re.sub(r'[^\w.]', '',orig_file)
        cleaned_file_name = cleaned_file_name.replace(' ', '_')
        
        return cleaned_file_name
