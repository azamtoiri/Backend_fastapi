from datetime import datetime
from pydantic import BaseModel
# TODO Response Model like ID->title->content->published->created_at


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    ...


class Post(PostBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
