from sqlalchemy import MetaData, Table, Column, Integer, String, Boolean, Float

metadata = MetaData()

user = Table(
    "user",
    metadata,
    Column("username", String, nullable=False),
    Column("password", String, nullable=False),
    Column("is_admin", Boolean, default=False, nullable=False),
    Column("balance", Float, default=0.0, nullable=False),
)

transport = Table(
    "transport",
    metadata,
    Column("id", Integer, primary_key=True),
)

rent = Table(
    "rent",
    metadata,
    Column("id", Integer, primary_key=True),
)
