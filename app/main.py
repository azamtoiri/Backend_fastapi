from fastapi import FastAPI
from app import endpoints

app = FastAPI()

app.include_router(endpoints.router)
