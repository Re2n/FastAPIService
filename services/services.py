from fastapi import Depends
from sqlalchemy import select

from models.models import ModelUser
from schemas.schemas import user, transport, rent
from schemas.db import database


class User:
    @classmethod
    async def register(cls, username, password):
        query = (
            user.insert()
            .values(
                username=username,
                password=password,
                is_admin=False,
                balance=0.0,
            )
            .returning(
                user.c.username,
                user.c.password,
            )
        )
        new_user = await database.fetch_one(query)
        new_user = dict(zip(new_user, new_user.values()))
        return new_user

    @classmethod
    async def update_user(cls, username, new_username, new_password):
        query = (
            user.update()
            .where(user.c.username == username)
            .values(
                username=new_username,
                password=new_password,
            )
        )
        return await database.execute(query)


class AdminUser:
    @classmethod
    async def get_users(cls):
        query = (
            select(
                [
                    user.c.username,
                    user.c.password,
                    user.c.is_admin,
                    user.c.balance,
                ]
            )
        )
        return await database.fetch_all(query)

    @classmethod
    async def get_user(cls, username):
        query = (
            select(
                [
                    user.c.username,
                    user.c.password,
                    user.c.is_admin,
                    user.c.balance,
                ]
            ).where(user.c.username == username)
        )
        return await database.fetch_one(query)

    @classmethod
    async def create_user(cls, new_user: ModelUser):
        query = (
            user.insert()
            .values(
                username=new_user.username,
                password=new_user.password,
                is_admin=new_user.is_admin,
                balance=new_user.balance,
            )
            .returning(
                user.c.username,
                user.c.password,
                user.c.is_admin,
                user.c.balance,
            )
        )
        new_user = await database.fetch_one(query)
        new_user = dict(zip(new_user, new_user.values()))
        return new_user

    @classmethod
    async def update_user(cls, username, update_user: ModelUser):
        query = (
            user.update()
            .where(user.c.username == username)
            .values(
                username=update_user.username,
                password=update_user.password,
                is_admin=update_user.is_admin,
                balance=update_user.balance,
            )
        )
        return await database.execute(query)

    @classmethod
    async def delete_user(cls, username):
        query = (
            user.delete()
            .where(user.c.username == username)
        )
        return await database.execute(query)