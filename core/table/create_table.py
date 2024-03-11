from sqlalchemy import create_engine, MetaData, Table, Column, String, Text, Integer, Float, BigInteger
from core.table.type_conversion import map_column_type



# 동적으로 테이블 생성하는 함수
def create_dynamic_table(table_name, columns_info):
    # 데이터베이스 연결 및 메타데이터 객체 생성
    engine = create_engine(
    "mariadb+pymysql://root:0000@localhost:3306/main")

    metadata = MetaData()

    columns = [Column(column_name, map_column_type(column_type), **column_options)
               for column_name, column_type, column_options in columns_info]
    table = Table(table_name, metadata, *columns)

    # 생성된 테이블을 데이터베이스에 반영
    metadata.create_all(engine)

    return table



# 컬럼 정보 예시: (컬럼 이름, 타입, 옵션)
columns_info = [
    ('id', 'UUID', {'primary_key': True}),
    ('name', 'Text', {}),
    ('age', 'Integer', {})
]
