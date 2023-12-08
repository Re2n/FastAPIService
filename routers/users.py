from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy import select

from models.models import ModelUser
from schemas.db import database
from schemas.schemas import user
from services.jwt import verify_jwt_token, create_jwt_token
from services.services import User, AdminUser

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/account/signin')

user_router = APIRouter(
    tags=['AccountController']
)


@user_router.post('/account/signup')
async def register(username, password, ):
    new_user = await User.register(username, password)
    return new_user


@user_router.post('/account/signin')
async def authenticate(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    query = (
        select(
            [
                user.c.username,
                user.c.is_admin,
                user.c.balance
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
    jwt_token = create_jwt_token(
        {"sub": cur_user['username'], 'is_admin': cur_user['is_admin'], 'balance': cur_user['balance']})
    return {'access_token': jwt_token}


async def get_current_user(token: str = Depends(oauth2_scheme)):
    decoded_data = verify_jwt_token(token)
    username = decoded_data.get('sub')
    is_admin = decoded_data.get('is_admin')
    balance = decoded_data.get('balance')
    if username is None:
        return {'data': 'Invalid token'}
    user = {'username': username, 'is_admin': is_admin, 'balance': balance}
    return user


@user_router.get('/account/me')
async def get_user_me(current_user: str = Depends(get_current_user)):
    return current_user


@user_router.put('/account/update')
async def update_user(new_username, new_password, current_user=Depends(get_current_user)):
    await User.update_user(current_user['username'], new_username, new_password)
    return {'status': 200}


adminuser_router = APIRouter(
    tags=['AdminAccountController']
)


@adminuser_router.get('/admin/account')
async def get_users(current_user=Depends(get_current_user)):
    if current_user['is_admin']:
        users = await AdminUser.get_users()
        return users
    return {'Not admin'}


@adminuser_router.get('/admin/account/{username}')
async def get_user(username, current_user=Depends(get_current_user)):
    if current_user['is_admin']:
        user = await AdminUser.get_user(username)
        return user
    return {'Not admin'}


@adminuser_router.post('/admin/account')
async def create_user(new_user: ModelUser, current_user=Depends(get_current_user)):
    if current_user['is_admin']:
        new_user = await AdminUser.create_user(new_user)
        return new_user
    return {'Not admin'}


@adminuser_router.put('/admin/account/{username}')
async def update_user(username, update_user: ModelUser, current_user=Depends(get_current_user)):
    if current_user['is_admin']:
        await AdminUser.update_user(username, update_user)
        return {'status': 200}
    return {'Not admin'}


@adminuser_router.delete('/admin/account/{username}')
async def delete_user(username, current_user=Depends(get_current_user)):
    if current_user['is_admin']:
        await AdminUser.delete_user(username)
        return {'status': 200}
    return {'Not admin'}