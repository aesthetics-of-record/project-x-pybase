from sqlalchemy import create_engine, MetaData, Table, Column, UUID, DATETIME, ARRAY
from core.table.util import to_column
from sqlalchemy.sql import func



# 동적으로 테이블 생성하는 함수
def create_table(table_name, columns_info):
    # 데이터베이스 연결 및 메타데이터 객체 생성
    engine = create_engine(
    "mariadb+mysqldb://root:0000@localhost:3306/main")

    metadata = MetaData()

    # 기본 columns
    # columns = [
    #     Column('id', UUID(as_uuid=True), primary_key=True),
    #     Column('created_at', DATETIME, default=func.now()),
    #     Column('updated_at', DATETIME, onupdate=func.now()),
    #     ]
    columns = []

    # 커스텀 column 추가
    for column_info in columns_info:
        columns.append(to_column(*column_info))

    table = Table(table_name, metadata, *columns)

    # 생성된 테이블을 데이터베이스에 반영
    metadata.create_all(engine)

    return table

# create_table('test4', '')

# engine = create_engine(
#     "mariadb+mysqldb://root:0000@localhost:3306/main")
# metadata = MetaData()
# table = Table('test3', metadata, autoload_with=engine)


# print(table.c.created_at)

# 컬럼 정보 예시: (컬럼 이름, 타입, 옵션)
columns_info = [
    ('id', 'UUID', {'primary_key': True}),
    ('name', 'Text', {}),
    ('age', 'Integer', {})
]
