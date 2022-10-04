from pydantic import BaseModel


class Post(BaseModel):
    title: str
    content: str
    published: bool = True

    class Config:
        orm_mode = True


class PostGet(Post):
    id: int
