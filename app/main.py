from fastapi import FastAPI
from app.routers import post, user, auth

app = FastAPI()

app.include_router(user.router)
app.include_router(post.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {"hello": "You are on main page"}
