from enum import Enum
from typing import Optional

from pydantic import BaseModel


class ModelUser(BaseModel):
    username: str
    password: str
    is_admin: bool
    balance: float


class ModelTransport(BaseModel):
    ownerusername: str
    canBeRented: bool
    transportType: str
    model: str
    color: str
    identifier: str
    description: Optional[str]
    latitude: float
    longitude: float
    minutePrice: Optional[float]
    dayPrice: Optional[float]


class UserModelTransport(BaseModel):
    canBeRented: bool
    transportType: str
    model: str
    color: str
    identifier: str
    description: Optional[str]
    latitude: float
    longitude: float
    minutePrice: Optional[float]
    dayPrice: Optional[float]


class RentModel(BaseModel):
    transportidentifier: str
    ownerusername: str
    timeStart: str
    timeEnd: Optional[str]
    priceOfUnit: float
    priceType: str
    finalPrice: Optional[float]
