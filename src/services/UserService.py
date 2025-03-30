from src.models.UserModel import UserModel
from fastapi.exceptions import HTTPException
from typing import List

class UserService: 
    @staticmethod
    async def adicionar_usuario(nome_usuario: str) -> UserModel:
        usuario = await UserModel.create(nome=nome_usuario)
        return usuario
    
    @staticmethod
    async def listar_usuarios() -> List[UserModel]:
        usuarios = await UserModel.all()
        if not usuarios:
            raise HTTPException(404, 'no users found error')
        return usuarios

    @staticmethod 
    async def usuario(id: int) -> UserModel:
        usuario = await UserModel.filter(id=id).first()
        if not usuario:
            raise HTTPException(404, 'user not found error')
        return usuario