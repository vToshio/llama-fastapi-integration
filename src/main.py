from src.routes.UsersRoutes import users
from src.routes.AIRoutes import ai
from tortoise.contrib.fastapi import register_tortoise
from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.db import *

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    await close_db()

app = FastAPI(lifespan=lifespan)
app.include_router(users)
app.include_router(ai)