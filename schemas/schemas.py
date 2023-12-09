from sqlalchemy import MetaData, Table, Column, Integer, String, Boolean, Float

metadata = MetaData()

user = Table(
    "user",
    metadata,
    Column("username", String, nullable=False, unique=True),
    Column("password", String, nullable=False),
    Column("is_admin", Boolean, default=False, nullable=False),
    Column("balance", Float, default=0.0, nullable=False),
)

transport = Table(
    "transport",
    metadata,
    Column("ownerusername", String, nullable=False),
    Column("canBeRented", Boolean, nullable=False),
    Column("transportType", String, nullable=False),
    Column("model", String, nullable=False),
    Column("color", String, nullable=False),
    Column("identifier", String, nullable=False),
    Column("description", String),
    Column("latitude", Float, nullable=False),
    Column("longitude", Float, nullable=False),
    Column("minutePrice", Float),
    Column("dayPrice", Float),
)

rent = Table(
    "rent",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("transportidentifier", String, nullable=False),
    Column("ownerusername", String, nullable=False),
    Column("timeStart", String, nullable=False),
    Column("timeEnd", String),
    Column("priceOfUnit", Float, nullable=False),
    Column("priceType", String, nullable=False),
    Column("finalPrice", Float),
)
