from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi import FastAPI
from core.migration.import_database import import_database
from models.import_json import import_json_model
from core.crud import CRUD
from core.database import get_all


app = FastAPI(title="zetabase",
              docs_url="/api/docs")
app.add_middleware(CORSMiddleware, allow_origins=["*"])


crud = CRUD()

@app.get("/")
async def root():
    a = get_all('migrations')
    return a


@app.post('/api/import')
async def migration_json(import_json: import_json_model):
    databases = [db.model_dump() for db in import_json]


    import_database(databases)
    return {"message": "마이그레이션 성공"}



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8000)
