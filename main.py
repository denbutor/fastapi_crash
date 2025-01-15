from fastapi import FastAPI
from contextlib import asynccontextmanager
from sqlalchemy.sql.operators import add
from database import create_tables, delete_tables
from router import router as tasks_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    print("Base is clear")
    await delete_tables()
    print("Base is ready")
    yield
    print("Turn Off")
app = FastAPI(lifespan=lifespan)
add.include_router(tasks_router)