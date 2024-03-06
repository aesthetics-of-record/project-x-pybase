from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# 세션 팩토리 캐싱을 위한 딕셔너리
_session_factories = {}


# 세션 객체 캐싱 함수
def _get_session_factory(db_name):
    # TODO : dbname 이 metadata 안에 존재하는 지 먼저 검증

    if db_name not in _session_factories:
        engine_url = f"mariadb+aiomysql://user:password@localhost:3307/{db_name}"
        engine = create_async_engine(engine_url)
        SessionFactory = sessionmaker(
            autoflush=False, expire_on_commit=False, bind=engine)
        _session_factories[db_name] = SessionFactory
    return _session_factories[db_name]


def get_session(db_name):
    SessionFactory = _get_session_factory(db_name)
    return SessionFactory
