import os, uuid
from sqlalchemy import (Column, Integer, MetaData, String, Table, create_engine, ARRAY)
from databases import Database

DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
metadata = MetaData()

user = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50), nullable=False),
    Column('email', String(200), nullable=False, index=True, unique=True),
)

database = Database(DATABASE_URI)
