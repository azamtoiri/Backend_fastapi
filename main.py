import uvicorn

from fastapi import FastAPI
from app.routers import post, user

app = FastAPI()

app.include_router(user.router)
app.include_router(post.router)

if __name__ == '__main__':
    uvicorn.run(app, host="", port=80)
