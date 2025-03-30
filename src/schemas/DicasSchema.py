from pydantic import BaseModel
from typing import List

class DicaRequest(BaseModel):
    categoria: str
    ambiente: str
    dispositivo: str    

class DicaResponse(BaseModel):
    titulo: str
    descricao: str

class DicasResponse(BaseModel):
    dicas: List[DicaResponse]