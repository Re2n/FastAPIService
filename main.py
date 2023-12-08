from fastapi import FastAPI
from routers import users
from schemas.db import database

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
