from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import select

# 데이터베이스 설정
DATABASE_URL = "mariadb+mysqldb://root:0000@localhost:3306/main"
engine = create_engine(DATABASE_URL)  # 동기 엔진 사용

# 비동기 엔진을 사용할 경우: async_engine = create_async_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
