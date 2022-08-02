from app.api.models import UserIn, UserOut, UserUpdate
from app.api.db import user, database


async def add_user(payload: UserIn):
    query = user.insert().values(**payload.dict())

    return await database.execute(query=query)

async def get_user(id):
    query = user.select(user.c.id==id)
    return await database.fetch_one(query=query)
