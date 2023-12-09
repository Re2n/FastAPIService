from fastapi import FastAPI
from routers import users, payment, transports, rent
from schemas.db import database
from services import auth

app = FastAPI(
    title="Trading App"
)


@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def startup():
    await database.disconnect()


app.include_router(users.user_router)
app.include_router(users.adminuser_router)
app.include_router(auth.router)
app.include_router(payment.payment_router)
app.include_router(transports.transport_router)
app.include_router(transports.user_transport_router)
app.include_router(rent.rent_router)
app.include_router(rent.user_rent_router)
