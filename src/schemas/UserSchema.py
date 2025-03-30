from pydantic import BaseModel

class UserCreateSchema(BaseModel):
    nome: str

class UserResponseSchema(BaseModel):
    id: int
    nome: str