from fastapi import Depends
from sqlalchemy import select


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


