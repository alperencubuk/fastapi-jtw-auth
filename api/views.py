from fastapi import APIRouter, Depends, HTTPException
from fastapi_jwt_auth import AuthJWT
from schemas import Login, Refresh, Token, User
from services import get_user
from utils import verify_password

router = APIRouter()


@router.post("/login", response_model=Login)
def login(user: Token, authorize: AuthJWT = Depends()):
    if user.username and user.password:
        db_user = get_user(user.username)
        if db_user and verify_password(user.password, db_user.password):
            access_token = authorize.create_access_token(subject=user.username)
            refresh_token = authorize.create_refresh_token(subject=user.username)
            return {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "token_type": "bearer",
            }
    raise HTTPException(status_code=401, detail="Bad username or password")


@router.post("/refresh", response_model=Refresh)
def refresh(authorize: AuthJWT = Depends()):
    authorize.jwt_refresh_token_required()

    current_user = authorize.get_jwt_subject()
    new_access_token = authorize.create_access_token(subject=current_user)
    return {"access_token": new_access_token, "token_type": "bearer"}


@router.get("/me", response_model=User)
def protected(authorize: AuthJWT = Depends()):
    authorize.jwt_required()

    current_user = authorize.get_jwt_subject()
    user = get_user(current_user)
    return User(**user.__dict__)
