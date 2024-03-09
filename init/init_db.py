from sqlalchemy import text, create_engine

# 생성할 데이터베이스 이름 목록
# 데이터베이스 한개에서 모든 테이블들을 관리할 예정
_databases = ["main"]

_engine = create_engine(
    "mariadb+pymysql://root:0000@localhost:3306")

# 각 데이터베이스에 대해 CREATE DATABASE 실행
for db_name in _databases:
    with _engine.connect() as connection:
        connection.execute(text(f"CREATE DATABASE IF NOT EXISTS {db_name}"))
        print(f"Database {db_name} created successfully")
