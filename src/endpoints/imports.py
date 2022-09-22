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


@router.get("/imports", response_model=List[schemas.ItemBase])
def get_imports(db: Session = Depends(get_db)):
    data = db.query(models.Item).all()
    return data


@router.post("/imports")
def post_imports(request: schemas.ItemBase, db: Session = Depends(get_db)):
    data = models.Item(id=request.id, url=request.url, parent_id=request.parent_id, type=request.type,
                       size=request.size, date=request.date)
    db.add(data)
    db.commit()
    db.refresh(data)
    return data


@router.get("/nodes/{node_id}")
def get_node_by_id():
    pass


@router.delete("/delete/{node_id}")
def delete_item():
    pass


@router.get("/updates")
def get_updates():
    pass


@router.get("/node/{id}/history")
def get_node_history():
    pass
