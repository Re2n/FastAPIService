from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy import select

from schemas.db import database
from schemas.schemas import user
from services.jwt import verify_jwt_token, create_jwt_token
from services.services import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/token')

router = APIRouter(
    tags=['AccountController']
)


@router.post('/register')
async def register(username, password):
    new_user = await User.register(username, password)
    return new_user


@router.post('/token')
async def authenticate(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    query = (
        select(
            [
                user.c.username,
            ]
        )
        .where(user.c.username == form_data.username)
    )
    cur_user = await database.fetch_one(query)
    if cur_user is None:
        return {'status': 400, 'data': 'Incorrect username or password'}
    query1 = (
        select(
            [
                user.c.password,
            ]
        )
        .where(user.c.username == form_data.username)
    )
    cur_password = await database.fetch_one(query1)
    if form_data.password != cur_password['password']:
        return {'status': 400, 'data': 'Incorrect username or password'}
    jwt_token = create_jwt_token({"sub": cur_user['username']})
    return {'access_token': jwt_token}


async def get_current_user(token: str = Depends(oauth2_scheme)):
    decoded_data = verify_jwt_token(token)
    username = decoded_data.get('sub')
    if username is None:
        return {'data': 'Invalid token'}
    return username


@router.get('/users/me')
async def get_user_me(current_user: str = Depends(get_current_user)):
    return current_user
