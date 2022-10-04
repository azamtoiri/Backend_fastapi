from typing import Optional, Literal, List
from enum import Enum
from pydantic import BaseModel


class ItemType(str, Enum):
    FOLDER = "FOLDER"
    FILES = "FILE"


class ItemBase(BaseModel):
    id: str
    url: Optional[str] = None
    parent_id: Optional[str] = None
    type: Optional[ItemType]
    size: Optional[int] = None

    class Config:
        orm_mode = True
        use_enum_values = True


class ItemImportRequest(BaseModel):
    items: List[ItemBase] = None
    updateDate: Optional[str] = None
