from datetime import datetime

from database import Base
from sqlalchemy import Column, DateTime, Integer, String
from utils import get_password_hash


class Model(Base):
    __abstract__ = True
    __tablename__ = ""

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    created: datetime = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated: datetime = Column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )


class User(Model):
    __tablename__ = "user"

    username: str = Column(String(length=32), nullable=False, unique=True, index=True)
    password: str = Column(String(length=64), nullable=False)
    email: str = Column(String(length=64), nullable=False, unique=True)

    def __init__(self, password: str, **kwargs):
        super(User, self).__init__(**kwargs)
        self.generate_password_hash(password)

    def generate_password_hash(self, password: str) -> None:
        self.password = get_password_hash(password)
