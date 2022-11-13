from database import session
from models import User


def get_user(username: str):
    with session() as db:
        return db.query(User).filter(User.username == username).one_or_none()
