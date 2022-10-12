from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

from .db.database import Base


class Post(Base):
    __tablename__ = 'post'

    id: int = Column(Integer, primary_key=True, nullable=False)
    owner_id: int = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    title: str = Column(String, nullable=False)
    content: str = Column(String, nullable=False)
    published: bool = Column(Boolean, server_default='TRUE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    owner = relationship("User")


class User(Base):
    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True, nullable=False)
    email: str = Column(String, nullable=False, unique=True)
    password: str = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
