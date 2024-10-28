from pydantic import BaseModel
from typing import List, Dict

class Create(BaseModel):
    name: str
    note: str

# class Update(BaseModel):
#     id: int = None
#     name: str = None
#     note: str = None