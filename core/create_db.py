from sqlalchemy import create_engine, text

engine = create_engine("mariadb+pymysql://root:aa04190825!!@localhost:3307/")

# 생성할 데이터베이스 이름 목록
databases = ["db1", "db2", "db3", "db4"]

# 각 데이터베이스에 대해 CREATE DATABASE 실행
for db_name in databases:
    with engine.connect() as connection:
        connection.execute(text(f"CREATE DATABASE IF NOT EXISTS {db_name}"))
        print(f"Database {db_name} created successfully")
        