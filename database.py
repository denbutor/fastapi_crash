from typing import Optional

from sqlalchemy import create_async_engine, Column
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from sqlalchemy.orm import sessionmaker
from sqlalchemy.testing.schema import mapped_column



engine = create_async_engine('sqlite+aiosqlite:///database.db')

new_session = async_sessionmaker(engine, expire_on_commit=False)

class Model(DeclarativeBase):
    pass

class TaskOrm(Model):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)

async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)
