from sqlalchemy import TEXT, FLOAT, BIGINT, UUID, INT, Enum, Column, Table, MetaData
from typing import List, Optional
from enum import Enum as Enum_Class
from models.migration import database_json_model
from core.exceptions import NotFoundException

# 컬럼 타입을 SQLAlchemy 타입으로 매핑
def to_column(column_name, column_type, column_options, enum_values: Optional[List[str]] = None,):
    if column_type == 'ENUM' and not (enum_values):
        raise ValueError(f"ENUM type need enum_values")

    if column_type == 'UUID':
        return Column(column_name, UUID(as_uuid=True), **column_options)
    elif column_type == 'TEXT':
        return Column(column_name, TEXT, **column_options)
    elif column_type == 'INT':
        return Column(column_name, INT, **column_options)
    elif column_type == 'BIGINT':
        return Column(column_name, BIGINT, **column_options)
    elif column_type == 'FLOAT':
        return Column(column_name, FLOAT, **column_options)
    elif column_type == 'ENUM':
        DynamicEnum = Enum_Class('ENUMCLASS', enum_values)
        return Column(column_name, Enum(DynamicEnum), **column_options)
    # 필요에 따라 더 많은 타입을 추가할 수 있습니다.
    else:
        raise ValueError(f"Unsupported column type: {column_type}")

def to_table(table_name, columns_info):
    
    metadata = MetaData()

    columns = []

    # 커스텀 column 추가
    for column_info in columns_info:
        columns.append(to_column(*column_info))

    table = Table(table_name, metadata, *columns)

    return table

    

def search_table(database_json: database_json_model, db_name: str, table_name: str):

    for db in database_json:
        # 특정 db
        if db.get('name') == db_name:

            for table in db.get('table_list'):
                # 특정 테이블
                if table.get('name') == table_name:
                    table_info = []
                    for schema in table.get('schema_list'):
                        table_info.append((schema.get('name'), schema.get('type'), schema.get('option'), schema.get("enum_values")))

                    return to_table(f"{db.get('name')}__{table.get('name')}", table_info)
                
    raise NotFoundException
