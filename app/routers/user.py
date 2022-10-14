from typing import List

from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session

from app.db.database import engine, get_db
from app import models, oauth2
from app import schemas
from app.utils import jwt_utils

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/users",
    tags=['Users']
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # hash_ password - user.password
    hashed_password = jwt_utils.hash_(user.password)
    user.password = hashed_password

    try:
        new_user = models.User(**user.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user
    except Exception as ex:
        print(ex)
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="This email already have been used")


@router.get("/", response_model=List[schemas.UserOut])
def get_users(db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    return db.query(models.User).all()


@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with {id} not founded")
    return user
