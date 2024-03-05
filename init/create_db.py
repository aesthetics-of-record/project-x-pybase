from sqlalchemy import text, func, DateTime, Uuid, TIMESTAMP, String, Boolean, UUID, Table, Column, Integer, MetaData, create_engine, Text
from db import engine
from uuid import uuid4

# 생성할 데이터베이스 이름 목록
_databases = ["auth"]

# 각 데이터베이스에 대해 CREATE DATABASE 실행
for db_name in _databases:
    with engine.connect() as connection:
        connection.execute(text(f"CREATE DATABASE IF NOT EXISTS {db_name}"))
        print(f"Database {db_name} created successfully")

# 메타데이터
metadata = MetaData()

_auth_engine = create_engine(
    "mariadb+pymysql://root:aa04190825!!@localhost:3307/auth")

# 테이블 정의
users_table = Table('users', metadata,
                    Column('id', UUID(as_uuid=True), primary_key=True),
                    Column('name', Text),
                    Column('age', Integer))

metadata.create_all(bind=_auth_engine)
