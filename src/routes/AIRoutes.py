from fastapi import APIRouter
from typing import List
from src.schemas.DicasSchema import *
from src.services.AIService import AIService
from fastapi.exceptions import HTTPException
import json  # Adicionar import para json

ai = APIRouter(prefix='/ai')

@ai.post('/gerar-dicas/')  # Ajustar o response_model para List[Dica]
async def gerar_dicas(request: DicaRequest):
    prompt = (
        f"Gere 5 dicas sustentáveis para otimizar o consumo de água, que sejam fáceis de se implementar e estejam "
        f"dentro dos parâmetros: categoria {request.categoria}, ambiente {request.ambiente} "
        f"e com o dispositivo de maior consumo sendo {request.dispositivo}. "
        f"Responda utilizando JSON, no formato: "
        f'[{{"titulo": "Dica 1", "descricao": "Descrição da dica 1"}}, ...]'
    )

    resposta_ia = await AIService.chamar_modelo(prompt)

    try: 
        dicas_json = json.loads(resposta_ia)  # Substituir eval por json.loads
        return dicas_json # Retorna a lista diretamente
    except json.JSONDecodeError as e:
        print(e)
        raise HTTPException(500, 'Erro ao decodificar a resposta da IA.')
    except Exception as e:
        print(e)
        raise HTTPException(500, 'Erro ao obter resposta da IA.')

