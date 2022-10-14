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
def post_imports(data: schemas.ItemImportRequest, db: Session = Depends(get_db)):
    length = len(data.items)
    for i in range(length):
        tmp = data.items[i]
        new_import = models.Item(id=tmp.id, url=tmp.url, parent_id=tmp.parent_id, type=tmp.type, date=data.updateDate)
        db.add(new_import)
        db.commit()
        db.refresh(new_import)
    return data.dict()


@router.get("/nodes/{id}")
def get_node_by_id(id: str, db: Session = Depends(get_db)):
    EXPECTED_TREE = {
        "type": "FOLDER",
        "id": "069cb8d7-bbdd-47d3-ad8f-82ef4c269df1",
        "size": 1984,
        "url": None,
        "parentId": None,
        "date": "2022-02-03T15:00:00Z",
        "children": [
            {
                "type": "FOLDER",
                "id": "1cc0129a-2bfe-474c-9ee6-d435bf5fc8f2",
                "parentId": "069cb8d7-bbdd-47d3-ad8f-82ef4c269df1",
                "size": 1600,
                "url": None,
                "date": "2022-02-03T15:00:00Z",
                "children": [
                    {
                        "type": "FILE",
                        "url": "/file/url3",
                        "id": "98883e8f-0507-482f-bce2-2fb306cf6483",
                        "parentId": "1cc0129a-2bfe-474c-9ee6-d435bf5fc8f2",
                        "size": 512,
                        "date": "2022-02-03T12:00:00Z",
                        "children": None,
                    },
                    {
                        "type": "FILE",
                        "url": "/file/url4",
                        "id": "74b81fda-9cdc-4b63-8927-c978afed5cf4",
                        "parentId": "1cc0129a-2bfe-474c-9ee6-d435bf5fc8f2",
                        "size": 1024,
                        "date": "2022-02-03T12:00:00Z",
                        "children": None
                    },
                    {
                        "type": "FILE",
                        "url": "/file/url5",
                        "id": "73bc3b36-02d1-4245-ab35-3106c9ee1c65",
                        "parentId": "1cc0129a-2bfe-474c-9ee6-d435bf5fc8f2",
                        "size": 64,
                        "date": "2022-02-03T15:00:00Z",
                        "children": None
                    }
                ]
            },
            {
                "type": "FOLDER",
                "id": "d515e43f-f3f6-4471-bb77-6b455017a2d2",
                "parentId": "069cb8d7-bbdd-47d3-ad8f-82ef4c269df1",
                "size": 384,
                "url": None,
                "date": "2022-02-02T12:00:00Z",
                "children": [
                    {
                        "type": "FILE",
                        "url": "/file/url1",
                        "id": "863e1a7a-1304-42ae-943b-179184c077e3",
                        "parentId": "d515e43f-f3f6-4471-bb77-6b455017a2d2",
                        "size": 128,
                        "date": "2022-02-02T12:00:00Z",
                        "children": None
                    },
                    {
                        "type": "FILE",
                        "url": "/file/url2",
                        "id": "b1d8fd7d-2ae3-47d5-b2f9-0f094af800d4",
                        "parentId": "d515e43f-f3f6-4471-bb77-6b455017a2d2",
                        "size": 256,
                        "date": "2022-02-02T12:00:00Z",
                        "children": None
                    }
                ]
            },
        ]
    }
    node = db.query(models.Item).filter(models.Item.id == id).first()
    return EXPECTED_TREE


@router.delete("/delete/{date}")
def delete_item(date: str, db: Session = Depends(get_db)):
    data = db.query(models.Item).filter(models.Item.date == date).first()
    return data


@router.get("/updates")
def get_updates():
    pass


@router.get("/node/{id}/history")
def get_node_history():
    pass
