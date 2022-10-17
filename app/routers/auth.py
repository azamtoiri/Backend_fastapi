from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.db.database import get_db
from app import models, oauth2, schemas
from app.utils import jwt_utils

router = APIRouter(tags=['Authentication'])


@router.post("/login", response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")

    if not jwt_utils.veryfi(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")

    access_toke = oauth2.create_access_token(data={"current_user": user.id})
    return {"access_token": access_toke, "token_type": "bearer"}
