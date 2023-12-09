from fastapi import APIRouter, Depends

from models.models import ModelUser

from services.services import User, AdminUser

from services.auth import get_current_user

user_router = APIRouter(
    tags=['AccountController']
)


@user_router.post('/account/signup')
async def register(username, password, ):
    new_user = await User.register(username, password)
    return new_user


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
