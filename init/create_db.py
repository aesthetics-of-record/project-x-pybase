from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column
from db import Base, engine

# 생성할 데이터베이스 이름 목록
_databases = ["_users"]

# 각 데이터베이스에 대해 CREATE DATABASE 실행
for db_name in _databases:
    with engine.connect() as connection:
        connection.execute(text(f"CREATE DATABASE IF NOT EXISTS {db_name}"))
        print(f"Database {db_name} created successfully")


class User(Base):
    __tablename__ = "notes"
    id: Mapped[str] = mapped_column(primary_key=True)
