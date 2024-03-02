import logging
import sys
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

import uvicorn
from core.config import settings
from core.database import sessionmanager
from fastapi import FastAPI

from core.database import DBSessionDep

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Function that handles startup and shutdown events.
    To understand more, read https://fastapi.tiangolo.com/advanced/events/
    """
    yield
    if sessionmanager._engine is not None:
        # Close the DB connection
        await sessionmanager.close()


app = FastAPI(lifespan=lifespan, title=settings.project_name,
              docs_url="/api/docs")
app.add_middleware(CORSMiddleware, allow_origins=["*"])


@app.get("/")
async def root():
    return {"message": "Async, FasAPI, PostgreSQL, JWT authntication, Alembic migrations Boilerplate"}


@app.get('/api/user')
def get_user(db: DBSessionDep):
    db.begin()

    return {"message": "성공"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8000)
