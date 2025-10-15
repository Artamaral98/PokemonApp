from pydantic import BaseModel, Field

class FavoritePayload(BaseModel):
    nome_pokemon: str = Field(..., min_length=1)