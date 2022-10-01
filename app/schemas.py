from pydantic import BaseModel
from typing import Optional, List


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None
