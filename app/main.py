from fastapi import FastAPI
from app.routers import post, user

app = FastAPI()

app.include_router(user.router)
app.include_router(post.router)


@app.get("/")
def root():
    return {"hello": "You are on main page"}
