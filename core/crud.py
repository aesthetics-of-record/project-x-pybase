from sqlalchemy import MetaData, Table, select
from sqlalchemy.orm import declarative_base
from core.database import SessionLocal, engine

class CRUD:
    def __init__(self, engine, session):
        self.metadata = MetaData()
        self.Base = declarative_base()
        self.engine = engine
        self.session = session

    def create_table_class(self, table_name: str):
        table = Table(table_name, self.metadata, autoload_with=self.engine)
        return type(table_name, (self.Base,), {'__table__': table})

    def model_to_dict(self, instance, keys):
        """모델 인스턴스와 속성 이름의 리스트를 받아, 순서가 지정된. 딕셔너리를 반환합니다."""
        return {key: getattr(instance, key, None) for key in keys}



    def get_list(self, table_name: str, offset: int, limit: int):
        """
        table_name(테이블명)
        offset(시작할 행)
        limit(반환할 결과 수)
        """
        Table = self.create_table_class(table_name)
        with self.session() as session:
            stmt = select(Table).limit(limit).offset(offset)
            results = session.execute(stmt).scalars().all()

            # 모델의 컬럼 순서를 유지하도록 딕셔너리 생성
            keys = Table.__table__.columns.keys()

            # 데이터를 순서가 지정된 딕셔너리로 변환하여 리스트에 추가
            ordered_data = [self.model_to_dict(instance, keys) for instance in results]
            
            return ordered_data

    # async def add(self, async_session: async_sessionmaker[AsyncSession], note: Note):
    #     """
    #     Create note object
    #     """
    #     async with async_session() as session:
    #         session.add(note)
    #         await session.commit()

    #     return note

    # async def get_by_id(
    #     self, async_session: async_sessionmaker[AsyncSession], note_id: str
    # ):
    #     """
    #     Get note by id
    #     """
    #     async with async_session() as session:
    #         statement = select(Note).filter(Note.id == note_id)

    #         result = await session.execute(statement)

    #         return result.scalars().one()

    # async def update(
    #     self, async_session: async_sessionmaker[AsyncSession], note_id, data
    # ):
    #     """
    #     Update note by id
    #     """
    #     async with async_session() as session:
    #         statement = select(Note).filter(Note.id == note_id)

    #         result = await session.execute(statement)

    #         note = result.scalars().one()

    #         note.title = data["title"]
    #         note.content = data["content"]

    #         await session.commit()

    #         return note

    # async def delete(self, async_session: async_sessionmaker[AsyncSession], note: Note):
    #     """delete note by id
    #     """
    #     async with async_session() as session:
    #         await session.delete(note)
    #         await session.commit()

    #     return {}