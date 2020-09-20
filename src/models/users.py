from sqlalchemy import Column, Integer, String

from src.db.base_class import Base


class Users(Base):
    id = Column(
        Integer,
        primary_key=True
    )
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
