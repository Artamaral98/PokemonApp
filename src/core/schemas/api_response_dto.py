from pydantic import BaseModel
from typing import TypeVar, Generic, Optional, List

T = TypeVar('T')
class ApiResponseDTO(BaseModel, Generic[T]):
    """
    Wrapper genérico para padronizar as respostas da API.
    """
    success: bool
    message: str
    data: Optional[T] = None
    errors: Optional[List[dict]] = None