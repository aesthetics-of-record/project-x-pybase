from pydantic import BaseModel
from typing import List, Optional

class Option(BaseModel):
    primary_key: bool
    nullable: bool
    unique: bool

class Schema(BaseModel):
    id: str
    name: str
    type: str
    option: Option
    enum_value_list: Optional[List[str]] = None

class Table(BaseModel):
    id: str
    name: str
    schema_list: List[Schema]

class Database(BaseModel):
    id: str
    name: str
    table_list: List[Table]

database_json_model = List[Database]