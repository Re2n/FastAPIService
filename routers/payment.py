from fastapi import APIRouter, Depends
from services.auth import get_current_user
from services.services import Payment

payment_router = APIRouter(
    tags=['PaymentController']
)


@payment_router.post('/payment/hesoyam/{username}')
async def admin_add_balance(username, balance: float, current_user=Depends(get_current_user)):
    if current_user['is_admin']:
        await Payment.add_balance(username, balance)
        return {'status': 200}
    return {'Not admin'}


@payment_router.post('/payment/hesoyam/')
async def user_add_balance(balance: float, current_user=Depends(get_current_user)):
    await Payment.add_balance(current_user['username'], balance)
    return {'status': 200}
