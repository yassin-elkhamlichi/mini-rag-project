from typing import Optional,Field
from bson.objectid import ObjectId
from pydantic import BaseModel


class Data_chunk(BaseModel):

  _id: Optional[ObjectId]
  chunk_text: str = Field(..., min_length=1, description="Text content of the data chunk")
  chunk_metadata: dict = Field(..., description="Metadata associated with the data chunk")
  chunk_order: int = Field(..., ge=0, description="Order of the chunk within the original file")
  chunk_project_id: str = Field(..., min_length=1, max_length=50, description="Identifier of the associated project")
  chunk_project_id: ObjectId

  class Config: # pydantic model configuration for unknown fields and json encoding
    arbitrary_types_allowed = True
 