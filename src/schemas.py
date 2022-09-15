# import string
from typing import Union
from enum import Enum
from pydantic import BaseModel


# region: Folders
#
# class FolderBase(BaseModel):
#     id: str
#     type: Union[str, None] = None
#     parent_id: Union[str, None] = None
#
#
# class FolderCreate(BaseModel):
#     items: list[FolderBase]
#     updateDate: str
#
#
# class FolderUpdate(FolderCreate):
#     ...
#
#
# class Folder(FolderUpdate):
#     class Config:
#         orm_mode = True


# endregion

# region: Files
"""
class FilesBase(BaseModel):
    parent_id: str
    url: str
    id: str
    size: int


class FilesCreate(FilesBase):
    ...


class FilesUpdate(FilesCreate):
    ...


class Files(FilesUpdate):
    ...

    class Config:
        orm_mode = True

"""


# endregion


class ItemType(str, Enum):
    FOLDER = "FOLDER"
    FILES = "FILES"


class Item:
    id: str
    url: Union[str] = None
    date: str
    parent_id: Union[str] = None
    type: ItemType
    size: Union[int] = None
    children: list

    class Config:
        orm_mode = True


class ItemImport(BaseModel):
    id: str
    url: Union[str] = None
    parent_id: Union[str] = None
    type: ItemType
    size: Union[int] = None


class ItemImportRequest(BaseModel):
    items: Union[list[ItemImport], None] = None
    updateDate: Union[str] = None


class ItemHistoryUnit(BaseModel):
    id: str
    url: Union[str] = None
    date: Union[str] = None
    parent_id: Union[str] = None
    type: ItemType
    size: Union[int] = None
    date: str


class ItemHistoryResponse(BaseModel):
    items: list[ItemHistoryUnit]


class Error(BaseModel):
    code: int
    message: str
