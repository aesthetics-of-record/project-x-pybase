from sqlalchemy import TEXT, FLOAT, BIGINT, UUID, INT, Enum
from typing import List, Optional
from enum import Enum as Enum_Class

# 컬럼 타입을 SQLAlchemy 타입으로 매핑


def map_column_type(column_type: str, enum_values: Optional[List[str]] = None):
    if column_type == 'ENUM' and not (enum_values):
        raise ValueError(f"ENUM type need enum_values")

    if column_type == 'UUID':
        return UUID(as_uuid=True)
    elif column_type == 'TEXT':
        return TEXT
    elif column_type == 'INT':
        return INT
    elif column_type == 'BIGINT':
        return BIGINT
    elif column_type == 'FLOAT':
        return FLOAT
    elif column_type == 'ENUM':
        DynamicEnum = Enum_Class('ENUMCLASS', enum_values)
        return Enum(DynamicEnum)
    # 필요에 따라 더 많은 타입을 추가할 수 있습니다.
    else:
        raise ValueError(f"Unsupported column type: {column_type}")
