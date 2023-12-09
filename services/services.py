from sqlalchemy import select

from models.models import ModelUser, ModelTransport, UserModelTransport, RentModel
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


class Payment:
    @classmethod
    async def add_balance(cls, username, balance):
        query = (
            user.update()
            .where(user.c.username == username)
            .values(
                balance=balance
            )
        )
        return await database.execute(query)


class AdminTransport:
    @classmethod
    async def create_transport(cls, new_transport: ModelTransport):
        query = (
            transport.insert()
            .values(
                ownerusername=new_transport.ownerusername,
                canBeRented=new_transport.canBeRented,
                transportType=new_transport.transportType,
                model=new_transport.model,
                color=new_transport.color,
                identifier=new_transport.identifier,
                description=new_transport.description,
                latitude=new_transport.latitude,
                longitude=new_transport.longitude,
                minutePrice=new_transport.minutePrice,
                dayPrice=new_transport.dayPrice,
            )
            .returning(
                transport.c.ownerusername,
                transport.c.canBeRented,
                transport.c.transportType,
                transport.c.model,
                transport.c.color,
                transport.c.identifier,
                transport.c.description,
                transport.c.latitude,
                transport.c.longitude,
                transport.c.minutePrice,
                transport.c.dayPrice,
            )
        )
        new_transport = await database.fetch_one(query)
        new_transport = dict(zip(new_transport, new_transport.values()))
        return new_transport

    @classmethod
    async def get_transports(cls):
        query = (
            select(
                [
                    transport.c.ownerusername,
                    transport.c.canBeRented,
                    transport.c.transportType,
                    transport.c.model,
                    transport.c.color,
                    transport.c.identifier,
                    transport.c.description,
                    transport.c.latitude,
                    transport.c.longitude,
                    transport.c.minutePrice,
                    transport.c.dayPrice,
                ]
            )
        )
        return await database.fetch_all(query)

    @classmethod
    async def get_transport(cls, identifier):
        query = (
            select(
                [
                    transport.c.ownerusername,
                    transport.c.canBeRented,
                    transport.c.transportType,
                    transport.c.model,
                    transport.c.color,
                    transport.c.identifier,
                    transport.c.description,
                    transport.c.latitude,
                    transport.c.longitude,
                    transport.c.minutePrice,
                    transport.c.dayPrice,
                ]
            ).where(transport.c.identifier == identifier)
        )
        return await database.fetch_one(query)

    @classmethod
    async def update_transport(cls, identifier, update_transport: ModelTransport):
        query = (
            transport.update()
            .where(transport.c.identifier == identifier)
            .values(
                ownerusername=update_transport.ownerusername,
                canBeRented=update_transport.canBeRented,
                transportType=update_transport.transportType,
                model=update_transport.model,
                color=update_transport.color,
                identifier=update_transport.identifier,
                description=update_transport.description,
                latitude=update_transport.latitude,
                longitude=update_transport.longitude,
                minutePrice=update_transport.minutePrice,
                dayPrice=update_transport.dayPrice,
            )
        )
        return await database.execute(query)

    @classmethod
    async def delete_transport(cls, identifier):
        query = (
            transport.delete()
            .where(transport.c.identifier == identifier)
        )
        return await database.execute(query)


class Transport:

    @classmethod
    async def get_transport(cls, identifier):
        query = (
            select(
                [
                    transport.c.ownerusername,
                    transport.c.canBeRented,
                    transport.c.transportType,
                    transport.c.model,
                    transport.c.color,
                    transport.c.identifier,
                    transport.c.description,
                    transport.c.latitude,
                    transport.c.longitude,
                    transport.c.minutePrice,
                    transport.c.dayPrice,
                ]
            ).where(transport.c.identifier == identifier)
        )
        return await database.fetch_one(query)

    @classmethod
    async def add_new_transport(cls, ownerusername, new_transport: UserModelTransport):
        query = (
            transport.insert()
            .values(
                ownerusername=ownerusername,
                canBeRented=new_transport.canBeRented,
                transportType=new_transport.transportType,
                model=new_transport.model,
                color=new_transport.color,
                identifier=new_transport.identifier,
                description=new_transport.description,
                latitude=new_transport.latitude,
                longitude=new_transport.longitude,
                minutePrice=new_transport.minutePrice,
                dayPrice=new_transport.dayPrice,
            )
        )
        return await database.fetch_one(query)

    @classmethod
    async def update_transport(cls, ownerusername, identifier, update_transport: UserModelTransport):
        query = (
            transport.update()
            .where(transport.c.identifier == identifier, transport.c.ownerusername == ownerusername)
            .values(
                ownerusername=ownerusername,
                canBeRented=update_transport.canBeRented,
                transportType=update_transport.transportType,
                model=update_transport.model,
                color=update_transport.color,
                identifier=identifier,
                description=update_transport.description,
                latitude=update_transport.latitude,
                longitude=update_transport.longitude,
                minutePrice=update_transport.minutePrice,
                dayPrice=update_transport.dayPrice,
            )
        )
        return await database.execute(query)

    @classmethod
    async def delete_transport(cls, identifier, ownerusername):
        query = (
            transport.delete()
            .where(transport.c.identifier == identifier, transport.c.ownerusername == ownerusername)
        )
        return await database.execute(query)


class AdminRent:

    @classmethod
    async def create_rent(cls, new_rent: RentModel):
        query = (
            rent.insert()
            .values(
                transportidentifier=new_rent.transportidentifier,
                ownerusername=new_rent.ownerusername,
                timeStart=new_rent.timeStart,
                timeEnd=new_rent.timeEnd,
                priceOfUnit=new_rent.priceOfUnit,
                priceType=new_rent.priceType,
                finalPrice=new_rent.finalPrice,
            )
            .returning(
                rent.c.transportidentifier,
                rent.c.ownerusername,
                rent.c.timeStart,
                rent.c.timeEnd,
                rent.c.priceOfUnit,
                rent.c.priceType,
                rent.c.finalPrice,
            )
        )
        new_rent = await database.fetch_one(query)
        new_rent = dict(zip(new_rent, new_rent.values()))
        return new_rent

    @classmethod
    async def get_rents_by_ownerusername(cls, ownerusername):
        query = (
            select(
                [
                    rent.c.transportidentifier,
                    rent.c.ownerusername,
                    rent.c.timeStart,
                    rent.c.timeEnd,
                    rent.c.priceOfUnit,
                    rent.c.priceType,
                    rent.c.finalPrice,
                ]
            )
            .where(rent.c.ownerusername == ownerusername)
        )
        rents = await database.fetch_all(query)
        return rents

    @classmethod
    async def get_rents_by_transportidentifier(cls, transportidentifier):
        query = (
            select(
                [
                    rent.c.transportidentifier,
                    rent.c.ownerusername,
                    rent.c.timeStart,
                    rent.c.timeEnd,
                    rent.c.priceOfUnit,
                    rent.c.priceType,
                    rent.c.finalPrice,
                ]
            )
            .where(rent.c.transportidentifier == transportidentifier)
        )
        rents = await database.fetch_all(query)
        return rents


class Rent:

    @classmethod
    async def get_free_cars(cls):
        query = (
            select(
                [
                    transport.c.ownerusername,
                    transport.c.canBeRented,
                    transport.c.transportType,
                    transport.c.model,
                    transport.c.color,
                    transport.c.identifier,
                    transport.c.description,
                    transport.c.latitude,
                    transport.c.longitude,
                    transport.c.minutePrice,
                    transport.c.dayPrice,
                ]
            )
            .where(transport.c.canBeRented == True)
        )
        free_cars = await database.fetch_all(query)
        return free_cars

    @classmethod
    async def get_my_rents(cls, username):
        query = (
            select(
                [
                    rent.c.transportidentifier,
                    rent.c.ownerusername,
                    rent.c.timeStart,
                    rent.c.timeEnd,
                    rent.c.priceOfUnit,
                    rent.c.priceType,
                    rent.c.finalPrice,
                ]
            )
            .where(rent.c.ownerusername == username)
        )
        my_rents = await database.fetch_all(query)
        return my_rents
