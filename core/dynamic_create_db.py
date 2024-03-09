from sqlalchemy import create_engine, MetaData, Table, Column, String, Text, Integer, Float, BigInteger
from sqlalchemy.dialects.postgresql import UUID, INET
import uuid

# 컬럼 타입을 SQLAlchemy 타입으로 매핑


def map_column_type(column_type):
    if column_type == 'UUID':
        return UUID(as_uuid=True)
    elif column_type == 'Text':
        return Text
    elif column_type == 'Integer':
        return Integer
    # 필요에 따라 더 많은 타입을 추가할 수 있습니다.
    else:
        raise ValueError(f"Unsupported column type: {column_type}")

# 동적으로 테이블 생성하는 함수


def create_dynamic_table(table_name, columns_info, metadata):
    columns = [Column(column_name, map_column_type(column_type), **column_options)
               for column_name, column_type, column_options in columns_info]
    table = Table(table_name, metadata, *columns)
    return table


# 데이터베이스 연결 및 메타데이터 객체 생성
engine = create_engine(
    "mariadb+pymysql://root:0000@localhost:3306/main", echo=True)
metadata = MetaData()

# 컬럼 정보 예시: (컬럼 이름, 타입, 옵션)
columns_info = [
    ('id', 'UUID', {'primary_key': True}),
    ('name', 'Text', {}),
    ('age', 'Integer', {})
]

# 동적 테이블 생성
dynamic_users_table = create_dynamic_table(
    'dynamic_users', columns_info, metadata)

# 생성된 테이블을 데이터베이스에 반영
metadata.create_all(engine)
