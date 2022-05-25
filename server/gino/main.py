# Описание базы данных
import os

from server.gino.models import db


async def create_db():
    await db.set_bind(os.environ["DATEBASE_URL"])
    await db.gino.create_all()