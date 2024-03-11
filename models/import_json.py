from pydantic import BaseModel
from typing import List

class Schema(BaseModel):
    id: str
    name: str
    type: str

class Table(BaseModel):
    id: str
    name: str
    schema: List[Schema]

class Database(BaseModel):
    id: str
    name: str
    table: List[Table]

import_json_model = List[Database]