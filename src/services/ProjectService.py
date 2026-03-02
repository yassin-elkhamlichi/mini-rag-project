from fastapi import UploadFile, status, HTTPException
from .BaseService import BaseService
from pathlib import Path

class ProjectService(BaseService):
    
    def __init__(self):
        super().__init__()

    def get_project_path(self, project_id):
      """
    Ensures the project directory exists and returns its Path object.

    Args:
        project_id (str): The unique identifier for the project.

    Returns:
        Path: The absolute path to the project directory.
    """
      project_dir = self.file_dir / project_id
    
    # will check if the dir exist or no
      project_dir.mkdir(parents=True, exist_ok=True)

      return project_dir
    
