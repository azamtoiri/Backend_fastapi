from typing import Optional, Literal
from enum import Enum
from pydantic import BaseModel


class ItemType(str, Enum):
    FOLDER = "FOLDER"
    FILES = "FILES"


class ItemBase(BaseModel):
    id: str
    url: Optional[str] = None
    date: str
    parent_id: Optional[str] = None
    type: Optional[ItemType]
    size: Optional[int] = None

    class Config:
        orm_mode = True
        use_enum_values = True


class ItemImportRequest(BaseModel):
    items: list[ItemBase] = None
    updateDate: Optional[str] = None
