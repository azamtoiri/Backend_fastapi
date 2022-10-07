from typing import List

from fastapi import APIRouter, Response, status, HTTPException, Depends
from sqlalchemy.orm import Session

from app.db.database import engine, get_db
from app import models
from app import schemas

models.Base.metadata.create_all(bind=engine)

router = APIRouter()


@router.get("/")
def root():
    return {"hello": "You are on main page"}


@router.get("/posts", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts


@router.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/posts/latest", response_model=schemas.PostBase)
def get_latest_post(db: Session = Depends(get_db)):
    last_post = db.query(models.Post).order_by(models.Post.created_at.desc()).first()
    return {"detail": last_post}


@router.get("/posts/{id}", response_model=schemas.Post)
def get_post_id(id: int, db: Session = Depends(get_db)):
    po_st = db.query(models.Post).filter(models.Post.id == id).first()
    if not po_st:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with {id} not fount")
    return po_st


@router.put("/posts/{id}")
def update_post(id: int, post: schemas.PostCreate, db: Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post_tmp = post_query.first()
    if post_tmp is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with {id} does not exist")
    post_query.update(post.dict(), synchronize_session=False)
    db.commit()

    return post_query.first()


@router.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):  # delete post
    post = db.query(models.Post).filter(models.Post.id == id)
    if post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with {id} does not exist")
    post.delete()
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
