from fastapi import APIRouter
from .urls import USER_CREATE_PATH, GET_USER, LOGIN_USER, LOGOUT_USER
import src.database.interaction as db

import bcrypt

from src.models.requests import (
    UserDataModel, LoginModel
)
from src.models.responses import (
    UserDataModelResponse
)
router = APIRouter()


@router.post(
    USER_CREATE_PATH,
    description="This end point helps to store user data in database"

)
def create_new_user(userData: UserDataModel) -> UserDataModelResponse:
    inserted_id = db.create_user(dict(userData))
    return {"status": "OK", "inserted_id": inserted_id}


@router.get(GET_USER)
def get_user(username: str, password: str):
    user_password = db.get_user(username)
    try:
        check = bcrypt.checkpw(password.encode(
            'utf-8'), user_password.encode('utf-8'))
    except:
        check = password == user_password

    return {"check": check}


@router.patch(LOGIN_USER)
def login_user(loginData: LoginModel):
    status = db.login(loginData.username, loginData.password)
    return {"state": status}


@router.patch(LOGOUT_USER)
def logout_user(email: str):
    status = db.logout(email)
    return {"state": status}
