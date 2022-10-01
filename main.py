import uvicorn

from fastapi import FastAPI
from app import endpoints

app = FastAPI()

app.include_router(endpoints.router)

if __name__ == '__main__':
    uvicorn.run(app, host="", port=80)