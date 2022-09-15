from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .constants import Connection


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


engine = create_engine(
    f"postgresql://{Connection.DATABASE_URL}",
)

Base = declarative_base()
SessionLocal = sessionmaker(engine, expire_on_commit=False)
