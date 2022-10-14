from fastapi import FastAPI

from app.routers import post, user, auth, vote

# models.Base.metadata.create_all(bind=engine)  # don't need any more because now we have alembic

app = FastAPI()

app.include_router(user.router)
app.include_router(post.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"hello": "You are on main page"}
