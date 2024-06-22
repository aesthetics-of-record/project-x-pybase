from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi import FastAPI
from core.migration.import_database import json_to_database
from models.migration import database_json_model
from core.crud import CRUD
from core.database import engine, SessionLocal
from core.table.util import search_table

app = FastAPI(title="zetabase")

app.add_middleware(CORSMiddleware, allow_origins=["*"])

crud = CRUD(engine, SessionLocal)

@app.get("/")
def root():
    a = crud.get_list('migrations', 0, 5) 

    return a


@app.post('/api/import')
def migration_json(import_json: database_json_model):
    databases = [db.model_dump() for db in import_json]

    # print(databases)
    json_to_database(databases)
    return {"message": "마이그레이션 성공"}


@app.post('/api/table')
def get_table(import_json: database_json_model):
    databases = [db.model_dump() for db in import_json]

    print(databases)

    a = search_table(databases, "db1", "table1").columns

    for i in a:
        print(i.primary_key)
        print(i.type)
        print(i.default)
    print(a)
    return "성공"



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8000)


