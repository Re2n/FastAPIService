from pydantic import BaseModel


class ModelUser(BaseModel):
    username: str
    password: str
    is_admin: bool
    balance: float
