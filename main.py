from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import async_sessionmaker

import uvicorn
from core.config import settings
from fastapi import FastAPI

from deprecated.database import engine

from sqlalchemy import MetaData, Table, and_, select

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     yield
#     if sessionmanager._engine is not None:
#         # Close the DB connection
#         await sessionmanager.close()


########### 만약 데이터베이스 스키마 형태 User 이 없을 경우에 #######
metadata = MetaData()
metadata.bind = engine

# 'users' 테이블을 메타데이터로 로드 (리플렉션)
users_table = Table('users', metadata, autoload_with=engine)
##################################################################


# create an async session object for CRUD
session = async_sessionmaker(bind=engine, expire_on_commit=False)


app = FastAPI(title=settings.project_name,
              docs_url="/api/docs")
app.add_middleware(CORSMiddleware, allow_origins=["*"])


@app.get("/")
async def root():
    return {"message": "Async, FasAPI, PostgreSQL, JWT authntication, Alembic migrations Boilerplate"}


@app.get('/api/user')
async def get_user():
    async with session() as session:
        statement = select(users_table).order_by(users_table.c.id)

    result = await session.execute(statement)

    return result.scalars()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8000)
