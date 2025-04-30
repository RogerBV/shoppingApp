from pydantic import BaseModel

class UpdateCategoryModel(BaseModel):
    id: int
    name: str