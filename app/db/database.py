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


# DATABASE_URL = f'postgresql://{Connection.DATABASE_URL}'
DATABASE_URL = f'{Connection.DATABASE_URL}'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
