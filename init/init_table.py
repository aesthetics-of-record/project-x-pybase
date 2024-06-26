from sqlalchemy import DateTime, Boolean, Table, Column, Integer, MetaData,  create_engine, Text, JSON, Enum, UUID

# 메타데이터
_metadata = MetaData()

_engine = create_engine(
    "mariadb+mysqlclient://root:0000@localhost:3306/main")


# 테이블 정의
users_table = Table('users', _metadata,
                    Column('id', UUID(as_uuid=True), primary_key=True),
                    Column('created_at', DateTime),
                    Column('updated_at', DateTime),
                    Column('email', Text),
                    Column('password', Text),
                    Column('name', Text),
                    Column('avatar_url', Text))

migrations_table = Table('migrations', _metadata,
                         Column('id', UUID(as_uuid=True), primary_key=True),
                         Column('created_at', DateTime),
                         Column('json', JSON))

# 테이블 적용
_metadata.create_all(bind=_engine, checkfirst=True)
