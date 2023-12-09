from typing import Annotated

from fastapi import Depends, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy import select

from schemas.db import database
from schemas.schemas import user
from services.jwt import create_jwt_token, verify_jwt_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/account/signin')
router = APIRouter()


@router.post('/account/signin')
async def authenticate(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    query = (
        select(
            [
                user.c.username,
                user.c.password,
                user.c.is_admin,
                user.c.balance,
            ]
        )
        .where(user.c.username == form_data.username)
    )
    cur_user = await database.fetch_one(query)
    if cur_user is None:
        return {'status': 400, 'data': 'Incorrect username or password'}
    if form_data.password != cur_user['password']:
        return {'status': 400, 'data': 'Incorrect username or password'}
    jwt_token = create_jwt_token(
        {"sub": cur_user['username'], 'is_admin': cur_user['is_admin'], 'balance': cur_user['balance']})
    return {'access_token': jwt_token, 'user': cur_user}


async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        decoded_data = verify_jwt_token(token)
        username = decoded_data.get('sub')
        is_admin = decoded_data.get('is_admin')
        balance = decoded_data.get('balance')
        if username is None:
            return {'data': 'Invalid token'}
        user = {'username': username, 'is_admin': is_admin, 'balance': balance}
        return user
    except:
        return {'Invalid user'}
