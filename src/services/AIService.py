from fastapi.exceptions import HTTPException
import httpx
import ollama

class AIService:
    _model_url = "http://localhost:11434/api/generate" 
    _model_name = "llama-sustentavel"

    @classmethod
    async def chamar_modelo(cls, prompt: str):
        """
        Faz a requisição ao modelo de IA e retorna a resposta.

        Args:
            prompt (str): Texto de entrada para o modelo de IA.

        Returns:
            str: Resposta gerada pelo modelo.

        Raises:
            HTTPException: Em caso de erro na requisição ou no processamento.
        """
        if not prompt or not prompt.strip():
            raise HTTPException(400, detail="O prompt não pode ser vazio.")

        try: 
            response = ollama.chat(
                model=cls._model_name,
                messages=[{
                    'role': 'user',
                    'content': prompt
                }],
                stream=False,
                format='json'
            )
            return response['message']['content']
        except httpx.RequestError as e:
            raise HTTPException(502, detail=f"Erro de conexão: {str(e)}")
        except KeyError:
            raise HTTPException(500, detail="Resposta inesperada do modelo.")
        except Exception as e:
            raise HTTPException(500, detail=str(e))