from fastapi import HTTPException, status
from .BaseService import BaseService
from .ProjectService import ProjectService
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.document_loaders import TextLoader
from models import Extension, ResponseMessage
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

class ProcessService(BaseService):
    
    def __init__(self, project_id: str):
        super().__init__()
        self.project_id = project_id
        self.project_path  = ProjectService().get_project_path(project_id=project_id)
      
    def get_file_extension(self, final_filename: str):
        return os.path.splitext(final_filename)[-1]

    def get_file_loader(self, final_filename: str):
        
        file_ex = self.get_file_extension(final_filename=final_filename)

        file_path = self.project_path / final_filename


        if file_ex == Extension.TXT.value:
            return TextLoader(file_path, encoding="utf-8")
        elif file_ex == Extension.PDF.value:
            return PyMuPDFLoader(file_path)
        
        return None
    
    def get_file_content(self, final_filename: str):
        loader = self.get_file_loader(final_filename=final_filename)
        if loader is None:
           raise HTTPException(
                status_code = status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
                detail = ResponseMessage.UNSUPPORTED_MEDIA_TYPE.value
            )
        return loader.load()

    def split_content(self, content_file: list, final_name: str, 
                      chunk_size: int=100, overlap_size: int=20):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=overlap_size,
            length_function=len,
            )
        
        file_content_text = [
            rec.page_content
            for rec in content_file
        ]
        file_metadata = [
            rec.metadata
            for rec in content_file
        ]

        chunks = text_splitter.create_documents(file_content_text, metadatas=file_metadata)
        return chunks