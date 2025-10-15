from pydantic import BaseModel, EmailStr, Field
from typing import TypeVar, Generic, Optional, List
from datetime import datetime
from pydantic import ConfigDict 


class RegisterPayload(BaseModel):
    nome: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="O nome deve ter entre 3 e 50 caracteres."
    )
    
    login: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="O login deve ter entre 3 e 50 caracteres."
    )
    
    email: EmailStr
    
    senha: str = Field(
        ...,
        min_length=4,
        description="A senha deve ter no mínimo 4 caracteres."
    )

class LoginPayload(BaseModel):
   
    login: str
    senha: str 


class UserResponseDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    IDUsuario: int
    Nome: str
    Login: str
    Email: EmailStr
    DtInclusao: datetime   