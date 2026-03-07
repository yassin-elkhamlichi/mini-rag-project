from typing import Optional,Field
from bson.objectid import ObjectId
from pydantic import BaseModel


class Project(BaseModel):
  _id: Optional[ObjectId]
  project_id: str = Field(..., min_length=1, max_length=50, description="Unique identifier for the project")

  class Config: # pydantic model configuration for unknown fields and json encoding
    arbitrary_types_allowed = True
 