from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, func

from src.utils.database import Base

from sqlalchemy.orm import relationship


class Item(Base):
    __tablename__ = "item"

    id: str = Column(String, primary_key=True, unique=True, nullable=False)
    url: str = Column(String(255), nullable=True)
    parent_id: str = Column(String, ForeignKey('folder.id'), nullable=True)
    type: str = Column(String, nullable=False)
    size: int = Column(Integer, default=0)


class Folder(Base):
    __tablename__ = "folder"

    id: str = Column(String, primary_key=True)
    item: str = Column(String)
    updateDate = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp(), nullable=False)
