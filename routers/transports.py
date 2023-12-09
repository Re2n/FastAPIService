from fastapi import APIRouter, Depends
from models.models import ModelTransport, UserModelTransport
from services.services import AdminTransport, Transport
from services.auth import get_current_user

transport_router = APIRouter(
    tags=['AdminTransportController']
)


@transport_router.post('/admin/transport')
async def create_transport(new_transport: ModelTransport, current_user=Depends(get_current_user)):
    if current_user['is_admin']:
        if new_transport.transportType in ['car', 'scooter', 'bike']:
            new_transport = await AdminTransport.create_transport(new_transport)
            return new_transport
        else:
            return {'Error'}
    return {'Not admin'}


@transport_router.get('/admin/transport')
async def get_transports(current_user=Depends(get_current_user)):
    if current_user['is_admin']:
        transports = await AdminTransport.get_transports()
        return transports
    return {'Not admin'}


@transport_router.get('/admin/transport/{identifier}')
async def get_transport(identifier, current_user=Depends(get_current_user)):
    if current_user['is_admin']:
        transports = await AdminTransport.get_transport(identifier)
        return transports
    return {'Not admin'}


@transport_router.put('/admin/trasport/{identifier}')
async def update_transport(identifier, update_transport: ModelTransport, current_user=Depends(get_current_user)):
    if current_user['is_admin']:
        if update_transport.transportType in ['car', 'scooter', 'bike']:
            await AdminTransport.update_transport(identifier, update_transport)
            return {'status': 200}
        else:
            return {'Error'}
    return {'Not admin'}


@transport_router.delete('/admin/transport/{identifier}')
async def delete_transport(identifier, current_user=Depends(get_current_user)):
    if current_user['is_admin']:
        await AdminTransport.delete_transport(identifier)
        return {'status': 200}
    return {'Not admin'}


user_transport_router = APIRouter(
    tags=['TransportController']
)


@user_transport_router.get('/transport/{identifier}')
async def get_transport(identifier, current_user=Depends(get_current_user)):
    transport = await Transport.get_transport(identifier)
    return transport


@user_transport_router.post('/transport')
async def add_new_transport(new_transport: UserModelTransport, current_user=Depends(get_current_user)):
    if new_transport.transportType in ['car', 'scooter', 'bike']:
        await Transport.add_new_transport(current_user['username'], new_transport)
        return {'status': 200}
    return {'Error'}


@user_transport_router.put('/transport/{identifier}')
async def update_transport(identifier, update_transport: UserModelTransport, current_user=Depends(get_current_user)):
    if update_transport.transportType in ['car', 'scooter', 'bike']:
        await Transport.update_transport(current_user['username'], identifier, update_transport)
        return {'status': 200}
    return {'Error'}


@user_transport_router.delete('/transport/{identifier}')
async def delete_transport(identifier, current_user=Depends(get_current_user)):
    await Transport.delete_transport(identifier, current_user['username'])
    return {'status': 200}
