from typing import List

from fastapi.requests import Request
from fastapi.responses import Response, RedirectResponse
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, HTTPException

from src.utils import crud
from src.db import models
from src import schemas
from src.utils.database import Base, get_db

router = APIRouter()


@router.get("/")
def docs():
    return RedirectResponse("/docs")


# @router.get("/imports/", response_model=List[models.Folder])
# def get_imports(item: schemas.ItemImportRequest, db: SessionLocal = Depends(get_db)):
#     return db

# @router.post("/imports/", response_model=schemas.Folder)
# def create_itme(item: schemas.ItemImportRequest, db: Session = Depends(get_db)):
#     db_folder = crud.create_item(db=db, imports=item)
#     if db_folder:
#         raise HTTPException(status_code=400)
#     return crud.create_item(db=db, imports=item)


@router.get("/imports/", response_model=schemas.ItemImportRequest)
def get_imports(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    item = crud.get_items(db, skip=skip, limit=limit)
    return item


@router.post("/imports/", response_model=schemas.ItemImportRequest)
def post_imports():
    pass


@router.get("/nodes/{node_id}", response_model=schemas.ItemImport)
def get_node_by_id():
    pass


@router.delete("/delete/{node_id}", response_model=schemas.ItemImportRequest)
def delete_item():
    pass


@router.get("/updates", response_model=schemas.ItemHistoryUnit)
def get_updates():
    pass


@router.get("/node/{id}/history", response_model=schemas.ItemHistoryUnit)
def get_node_history():
    pass
