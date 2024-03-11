from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import select

# 데이터베이스 설정
DATABASE_URL = "mariadb+pymysql://root:0000@localhost:3306/main"
engine = create_engine(DATABASE_URL)  # 동기 엔진 사용

# 비동기 엔진을 사용할 경우: async_engine = create_async_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

metadata = MetaData()
Base = declarative_base()

# 동적으로 테이블 클래스 생성
def create_dynamic_table_class(table_name: str):
    table = Table(table_name, metadata, autoload_with=engine)
    return type(table_name, (Base,), {'__table__': table})

def model_to_dict(instance, keys):
    """모델 인스턴스와 속성 이름의 리스트를 받아, 순서가 지정된 딕셔너리를 반환합니다."""
    return {key: getattr(instance, key, None) for key in keys}

def get_all(table_name: str):
    DynamicTable = create_dynamic_table_class(table_name)
    with SessionLocal() as session:
        stmt = select(DynamicTable)
        result = session.execute(stmt)
        data = result.scalars().all()

        # 모델의 컬럼 순서를 유지하도록 딕셔너리 생성
        keys = DynamicTable.__table__.columns.keys()
        return [model_to_dict(row, keys) for row in data]
