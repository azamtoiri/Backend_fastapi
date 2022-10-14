from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.utils.constants import Connection


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


SQLALCHEMY_DATABASE_URL = f'postgresql://{Connection.DATABASE_USERNAME}' \
                          f':{Connection.DATABASE_PASSWORD}@{Connection.DATABASE_HOSTNAME}' \
                          f':{Connection.DATABASE_PORT}/{Connection.DATABASE_NAME}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
