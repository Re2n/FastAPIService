from fastapi import APIRouter, Depends
from models.models import RentModel
from services.services import AdminRent, Rent
from services.auth import get_current_user

rent_router = APIRouter(
    tags=['AdminRentController']
)


@rent_router.post('/admin/rent')
async def create_rent(new_rent: RentModel, current_user=Depends(get_current_user)):
    if current_user['is_admin']:
        if new_rent.priceType in ['minutes', 'days']:
            new_rent = await AdminRent.create_rent(new_rent)
            return new_rent
        else:
            return {'Error'}
    return {'Not admin'}


@rent_router.get('/admin/userhistory/{username}')
async def get_rents_by_username(username, current_user=Depends(get_current_user)):
    if current_user['is_admin']:
        rents = await AdminRent.get_rents_by_ownerusername(username)
        return rents
    return {'Not admin'}


@rent_router.get('/admin/transporthistory/{transportidentifier}')
async def get_rents_by_transportidentifier(transportidentifier, current_user=Depends(get_current_user)):
    if current_user['is_admin']:
        rents = await AdminRent.get_rents_by_transportidentifier(transportidentifier)
        return rents
    return {'Not admin'}


user_rent_router = APIRouter(
    tags=['RentController']
)


@user_rent_router.get('/rent/transport')
async def get_free_cars():
    free_cars = await Rent.get_free_cars()
    return free_cars


@user_rent_router.get('/rent/myhistory')
async def get_my_rents(current_user=Depends(get_current_user)):
    my_rents = await Rent.get_my_rents(current_user['username'])
    return my_rents
