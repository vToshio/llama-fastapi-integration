from fastapi import APIRouter
from src.models.UserModel import UserModel
from src.schemas.UserSchema import *
from src.services.UserService import UserService
from typing import List

users = APIRouter(prefix='/users')

@users.post('/create/', response_model=UserResponseSchema)
async def create_user(user: UserCreateSchema):
    user = await UserService.adicionar_usuario(user.nome)
    return user

@users.get('/list/', response_model=List[UserResponseSchema])
async def get_users():
    users = await UserService.listar_usuarios()
    return users

@users.get('/{id}/', response_model=UserResponseSchema)
async def get_user(id: int):
    user = await UserService.usuario(id)
    return user
    