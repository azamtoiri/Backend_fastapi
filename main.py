import uvicorn

from fastapi import FastAPI
from src.endpoints import imports
from fastapi.staticfiles import StaticFiles

from src.utils.database import engine, Base

app = FastAPI()

app.include_router(imports.router)

if __name__ == '__main__':
    uvicorn.run(app, host="", port=80)