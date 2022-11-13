from typing import Optional

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker
from sqlalchemy.util.compat import contextmanager

DATABASE_URL = "postgresql://user:password@database:5432/alpha"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


def get_db() -> Optional[Session]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


session = contextmanager(get_db)
